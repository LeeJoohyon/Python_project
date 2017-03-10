result = parser.get_start_end_offset_list(webtoon_id)

f = open('webtoon.html', 'w')
f.write('<html><body>')
for item in result:
    f.write('''
<div>
    <a href="{href}">{title}</a>
    <span>{created}</span>

</div> '''.format(
        href=item['link'],
        title=item['title'],
        created=item['created'],
    ))
f.write('</body></html></body>')
f.close()
f.close()