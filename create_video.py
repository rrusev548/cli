import os, subprocess, textwrap
os.makedirs('fire_story_frames', exist_ok=True)
blocks = [
('HOOK','Първата искра','Мълния оставя жив въглен в сухата трева.'),
('BUILD','Малък въглен','В тъмнината той можел да изгасне всеки момент.'),
('BUILD','Сухи клонки','Клонките поддържат пламъка; вятърът го разпалва.'),
('BUILD','Да го пренесеш','Първото умение: да не оставиш огъня да умре.'),
('BUILD','Трудни следи','Пепелта и овъгленият камък не разказват всичко.'),
('BUILD','Wonderwerk','Пещера в Южна Африка: горене преди около милион години.'),
('BUILD','Използван, не запален','Следите показват употреба и вероятно пазене.'),
('BUILD','Gesher Benot Ya’aqov','Изгорени семена, дърво и кремък — преди 790 000 години.'),
('BUILD','Първите огнища','Концентрираните въглени приличат на огнища.'),
('BUILD','Храна край огъня','Маслина, див ечемик и грозде — растения за ядене.'),
('BUILD','Център на групата','Въгленът се превръща в място за събиране.'),
('BUILD','Светлина','След залез пещерата става пространство за работа.'),
('BUILD','Топлина и защита','Огънят прогонва студа и плаши част от хищниците.'),
('BUILD','Готвене','Топлината омекотява месото и растенията.'),
('BUILD','Малки успехи','Наблюдение, грешка, повторение — така се учи.'),
('BUILD','Живот около огъня','Хората започват да организират деня си около него.'),
('TURN','Огънят има бъдеще','Камъни, дърва и един въглен за утрото.'),
('CLOSER','От искра до огнище','Хората не откриват огъня — научават се да го управляват.')]
for i,(tag,title,desc) in enumerate(blocks,1):
    glow = '#ffcc66' if i<4 else '#ff8a3d'
    emberx = 260 + i*34
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
<rect width="1280" height="720" fill="#121622"/><circle cx="1060" cy="110" r="90" fill="#20283a" opacity=".6"/>
<path d="M0 570 Q180 520 350 575 T700 560 T1020 570 T1280 550 V720 H0Z" fill="#202638"/>
<text x="72" y="84" fill="#f4b860" font-family="DejaVu Sans" font-size="22" letter-spacing="5">{tag}  /  {i:02d}</text>
<text x="72" y="150" fill="#fff6e7" font-family="DejaVu Sans" font-weight="bold" font-size="48">{title}</text>
<text x="72" y="205" fill="#bcc5d6" font-family="DejaVu Sans" font-size="25">{desc}</text>
<!-- faceless stick figures -->
<g stroke="#dce3ef" stroke-width="11" fill="none" stroke-linecap="round" stroke-linejoin="round">
<circle cx="450" cy="414" r="34"/><path d="M450 450v105m-55-65 55 30 55-28m-55 63-48 70m48-70 48 70"/>
<circle cx="660" cy="410" r="34"/><path d="M660 446v110m-55-66 55 28 60-45m-60 83-45 71m45-71 55 71"/>
<circle cx="850" cy="430" r="34"/><path d="M850 466v100m-48-52 48 25 52-26m-52 53-42 66m42-66 45 66"/>
</g>
<!-- fire and shared ember -->
<ellipse cx="650" cy="610" rx="170" ry="25" fill="#090b12"/><path d="M560 610 Q600 565 610 490 Q655 535 650 445 Q715 520 704 570 Q760 540 738 610Z" fill="#ff6b35"/><path d="M610 610 Q640 570 645 520 Q680 555 676 600Z" fill="#ffd166"/><circle cx="{emberx}" cy="588" r="10" fill="{glow}"/><path d="M450 585 Q530 625 650 610" stroke="#f4b860" stroke-width="4" opacity=".45"/>
<text x="72" y="665" fill="#f4b860" font-family="DejaVu Sans" font-size="18">ЕДИН ВЪГЛЕН • ЕДНА ГРУПА • ЕДНА ДЪЛГА ИСТОРИЯ</text>
</svg>'''
    open(f'fire_story_frames/frame_{i:02d}.svg','w').write(svg)
    pass
# Frames are SVG for crisp, browser-rendered 2D animation; fire_story.html assembles them into a 180-second timeline.
