import codecs
import markdown

md_file = codecs.open('getting-started-with-fontForge.md', "r", encoding="utf-8");
template_file = codecs.open('template.html', "r", encoding="utf-8");
html_file = codecs.open('index.html', "w", encoding="utf-8");

html = template_file.read().replace('{{md_converted}}',
                                    markdown.markdown(md_file.read(), 
                                    output_format='html5'))
html_file.write(html)
md_file.close()
template_file.close()
html_file.close()
