"""Quantitative figure-overlap audit: text-on-text and line-through-text."""
import fitz

NAMES = ["fig_two_floors", "fig_interruption_phases", "fig_event_loop", "fig_tool_hiding"]


def seg_len(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


def dist_point_seg(p, a, b, eps=1e-9):
    ax, ay, bx, by, px, py = a.x, a.y, b.x, b.y, p.x, p.y
    dx, dy = bx - ax, by - ay
    if dx * dx + dy * dy < eps:
        return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    return ((px - (ax + t * dx)) ** 2 + (py - (ay + t * dy)) ** 2) ** 0.5


def _segments(dr):
    """Flatten a drawing into straight segments (lines, rect edges, curves)."""
    segs = []
    for item in dr["items"]:
        if item[0] == "l":
            p1, p2 = item[1], item[2]
            if seg_len(p1, p2) > 3:
                segs.append((p1, p2))
        elif item[0] == "re":
            r = item[1]
            q = [r.bl, r.br, r.tr, r.tl, r.bl]
            for k in range(4):
                if seg_len(q[k], q[k + 1]) > 3:
                    segs.append((q[k], q[k + 1]))
        elif item[0] in ("c", "q", "be"):
            raw = item[1]
            if isinstance(raw, dict):
                pts = [raw[k] for k in ("from", "c1", "c2", "to") if k in raw]
                pts += [raw[k] for k in ("from", "c", "to") if k in raw]
            elif raw and isinstance(raw[0], (int, float)):
                pts = [fitz.Point(raw[k], raw[k + 1])
                       for k in range(0, len(raw) - 1, 2)]
            else:
                pts = list(raw)
            pts = [p if hasattr(p, "x") else fitz.Point(float(p[0]), float(p[1]))
                   for p in pts]
            for k in range(len(pts) - 1):
                if seg_len(pts[k], pts[k + 1]) > 3:
                    segs.append((pts[k], pts[k + 1]))
    return segs


def audit(path):
    doc = fitz.open(path)
    problems = []
    for pno, page in enumerate(doc):
        fig = NAMES[pno] if pno < len(NAMES) else f"page{pno+1}"
        spans = []
        d = page.get_text("dict")
        for blk in d["blocks"]:
            for ln in blk.get("lines", []):
                for s in ln.get("spans", []):
                    spans.append((fitz.Rect(s["bbox"]), s["text"]))
        # text-text overlaps
        for i in range(len(spans)):
            for j in range(i + 1, len(spans)):
                r1, t1 = spans[i]
                r2, t2 = spans[j]
                inter = r1 & r2
                area = inter.get_area() if not inter.is_empty else 0.0
                if area > 4.0:
                    problems.append(
                        f"{fig} TEXT-TEXT [{t1!r}] x [{t2!r}] area={area:.0f}")
        # straight segments + rect edges (+ coarse curve chords)
        segs = []
        for dr in page.get_drawings():
            segs.extend(_segments(dr))
        # line-through-text
        for r, t in spans:
            cx, cy = r.x0 + r.width / 2, r.y0 + r.height / 2
            c = fitz.Point(cx, cy)
            for a, b in segs:
                d0 = dist_point_seg(c, a, b)
                if d0 < 3.0:
                    problems.append(
                        f"{fig} LINE-TEXT [{t!r}] vs seg "
                        f"({a.x:.0f},{a.y:.0f})-({b.x:.0f},{b.y:.0f}) d={d0:.1f}")
    return problems


if __name__ == "__main__":
    ps = audit("fig_preview.pdf")
    if ps:
        print("OVERLAPS: %d" % len(ps))
        for p in ps:
            print(" -", p)
    else:
        print("No overlaps detected.")
