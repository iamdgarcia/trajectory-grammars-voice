import re, sys
from decimal import Decimal

def rects_from_page(page_dict):
    """Extract (bbox, text, font_size) for text spans; (bbox, stroke?) for lines/curves."""
    from pdfminer.pdftypes import resolve1
    from pdfminer.layout import LTTextLine, LTTextLineHorizontal, LTCurve, LTLine, LTRect, LTTextContainer, LTChar
    out = []
    def walk(o):
        from pdfminer.layout import LTContainer
        if isinstance(o, LTTextLineHorizontal):
            txt = o.get_text().strip()
            if txt:
                out.append(('text', (o.x0, o.y0, o.x1, o.y1), txt))
        elif isinstance(o, (LTCurve, LTLine, LTRect)):
            out.append(('line', (o.x0, o.y0, o.x1, o.y1), ''))
        if isinstance(o, LTContainer):
            for c in o:
                walk(c)
    walk(page_dict)
    return out

def intersects(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])

def shrink(r, f=1.5):
    return (r[0]+f, r[1]+f, r[2]-f, r[3]-f)

def main(pdf, page_num):
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LTContainer
    pages = list(extract_pages(pdf, page_numbers=[page_num-1]))
    items = rects_from_page(pages[0])
    texts = [(r, t) for k, r, t in items if k == 'text']
    lines = [r for k, r, t in items if k == 'line']
    # 1) text-text overlaps
    tt = []
    for i in range(len(texts)):
        for j in range(i+1, len(texts)):
            a, b = texts[i][0], texts[j][0]
            if intersects(shrink(a), shrink(b)):
                ov = min(a[2], b[2]) - max(a[0], b[0])
                ovh = min(a[3], b[3]) - max(a[1], b[1])
                if ov > 1.0 and ovh > 1.0:
                    tt.append((texts[i][1][:40], texts[j][1][:40], round(ov,1), round(ovh,1)))
    # 2) line-through-text
    lt = []
    for k, r, t in [(k,r,t) for k,r,t in items if k=='line']:
        for tr, tt_ in texts:
            if len(tt_) > 2 and intersects(shrink((tr[0],tr[1],tr[2],tr[3])), (r[0]+0.5, r[1]+0.5, r[2]-0.5, r[3]-0.5)):
                # line passes through text box (both dims meaningful)
                w = min(r[2], tr[2]) - max(r[0], tr[0])
                h = min(r[3], tr[3]) - max(r[1], tr[1])
                if w > 2 and h > 2:
                    lt.append((tt_[:40], [round(x,1) for x in r]))
    print(f"== page {page_num}: {len(texts)} text spans, {len(lines)} line/curve items")
    print(f"text-text overlaps ({len(tt)}):")
    for a, b, ow, oh in tt[:25]:
        print(f"  {a!r} X {b!r} ov=({ow},{oh})")
    print(f"line-through-text hits ({len(lt)}):")
    seen = set()
    for t, r in lt[:40]:
        key = (t, tuple(r))
        if key in seen: continue
        seen.add(key)
        print(f"  {t!r} <- line {r}")

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
