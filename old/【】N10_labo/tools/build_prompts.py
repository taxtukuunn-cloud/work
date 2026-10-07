# N10 Lab のプロンプト一覧（Lab_prompts.json）を組み立てる
import json
Q='masterpiece, best quality, amazing quality, very aesthetic, absurdres'
NEG_BASE=('lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, numbers, sign, logo, '
 'child, loli, shota, young, teenage, underage, childlike body, '
 'twins, same face, same hair color, extra legs, three legs, four legs, extra arms, merged bodies')
NEG_H=(', muscular, abs, pectorals, bara, hairy, broad shoulders, big body, tall man, huge penis, eyes visible on the man, 2boys, '
 'collar, choker, leash, futanari, vaginal, pussy, penetration by male, nude female, female nudity, cowgirl position, '
 'merged, fused, overlapping penises, penis touching penis, penis on female, strap-on')
NEG_DEV=', giant dildo, oversized dildo, deeply inserted, fully inserted, buried inside'
HERO=('1boy, faceless male, black hair, short hair, hair over eyes, bangs covering eyes, adult male, adult body proportions, '
 'androgynous, feminine body, petite, slender, narrow shoulders, narrow waist, thin arms, smooth pale skin, no muscles, blush, height difference')
CH={
 'SHIORI':'1girl, mature female, adult woman, tall, silver hair, short hair, messy hair, red eyes, goggles on head, white lab coat, black turtleneck, dark grey pants, cold expression, half-closed eyes, medium breasts',
 'MINASE':'1girl, adult woman, light grey hair, bob cut, light blue eyes, white lab coat, grey blouse, holding a tablet computer, expressionless, small breasts',
 'CHLOE':'1girl, adult woman, dark blue hair, short hair, purple eyes, white lab coat, black gloves, leather straps hanging at her waist, expressionless, small breasts',
 'HAKU':'1girl, adult woman, white hair, high ponytail, green eyes, white lab coat, sleeves rolled up, holding a clipboard, curious grin, medium breasts',
 'LX01':'no humans, large mechanical device, prototype machine, not humanoid, white and grey metal armor, multiple robotic arms, one large glowing red lens',
}
DESC={'SHIORI':'the silver-haired scientist in a white lab coat','MINASE':'the grey-haired assistant with a bob cut in a white lab coat',
 'CHLOE':'the dark-blue-haired guide in a white lab coat and black gloves','HAKU':'the white-haired woman with a ponytail in a white lab coat',
 'LX01':'the large white prototype machine with robotic arms and a red lens'}
ROOM={
 'bg':'indoors, abandoned research laboratory, long white corridor, cracked windows, pale blue fluorescent lights, old monitors, cables on the floor, detailed background',
 'm1':'indoors, measurement room, reclining examination chair with soft straps, wall of monitors showing waveform graphs, pale blue lighting, detailed background',
 'm2':'indoors, treatment room, padded kneeling examination table, steel instrument tray, white tiles, pale blue lighting, detailed background',
 'm3':'indoors, all-white conditioning room, deep white chair, small speakers built into the walls, control box with knobs, detailed background',
 'wait':'indoors, small waiting room, grey sofa, three wall monitors, ceiling cameras with red lamps, dim lighting, detailed background',
 'rec':'indoors, record room, walls covered with monitors showing graphs, white chair in the center, dim blue light, detailed background',
 'e2':'indoors, restraint room, body-shaped padded table with many leather straps, rows of leather straps hanging on the wall, detailed background',
 'e3':'indoors, specimen storage room, walls of small steel drawers, padded kneeling table, detailed background',
 'boss':'indoors, dark hangar laboratory, cables hanging from the ceiling, red light, metal floor, detailed background',
}
P=[]
def add(key,seed,safety,body,neg='',trans=False):
    P.append({'key':key,'file':key+'.png','seed_name':seed,'transparent_background':trans,
      'positive':f'{Q}, {safety}, {body}','negative':NEG_BASE+neg})
def portrait(key,seed,body):
    add(key,seed,'safe',body+', standing, full body, looking at viewer, simple background, white background',', 1boy, nude',True)
def woman_scene(key,who,safety,room,scene,sentence,neg=NEG_H+NEG_DEV):
    add(key,who,safety,f'{CH[who]}, {HERO}, {scene}, cfnm, clothed female, nude male, only the man is naked, the woman keeps all her clothes on, {ROOM[room]}, {sentence}',neg)
def boss_scene(key,safety,room,scene,sentence):
    add(key,'LX01',safety,f'{HERO}, solo male, {CH["LX01"].replace("no humans, ","")}, mechanical arms, {scene}, nude male, {ROOM[room]}, {sentence}',NEG_H+NEG_DEV+', 1girl, female, humanoid robot, android girl')
def onani(key,who,room,scene,sentence):
    other=CH[who] if who!='LX01' else CH['LX01'].replace('no humans, ','')
    add(key,'HERO','explicit',f'{HERO}, nude male, solo focus, he is in the foreground, {scene}, masturbation, flushed, sweat, trembling, {DESC[who]} far in the background watching, small in frame, not touching him, {other}, {ROOM[room]}, {sentence}',NEG_H+NEG_DEV+', woman touching him, hetero sex')

# 立ち絵・背景
portrait('Lab_master','SHIORI',f'{CH["SHIORI"]}, solo, hands in coat pockets')
portrait('Lab_e1','MINASE',f'{CH["MINASE"]}, solo, looking at the tablet')
portrait('Lab_e2','CHLOE',f'{CH["CHLOE"]}, solo, holding a leather wrist cuff')
portrait('Lab_e3','HAKU',f'{CH["HAKU"]}, solo, holding a metal speculum tool, one eye closed')
portrait('Lab_boss','LX01',f'{CH["LX01"]}, robotic arms spread out, sci-fi')
add('Lab_bg','BG','safe','no humans, scenery, '+ROOM['bg'])

S='The {d} {v} while the small slim naked man {h}.'
def s(who,v,h): return S.format(d=DESC[who],v=v,h=h)
# マスター技・モンスター技
woman_scene('Lab_atk_m1','SHIORI','explicit','m1','from side, he reclines on the examination chair, wrists strapped, transparent suction cups attached to his nipples, thin tubes, stretched nipples, she turns a dial on the machine, arched back',s('SHIORI','adjusts the suction machine','is strapped to the chair with suction cups on his nipples'))
woman_scene('Lab_atk_m2','SHIORI','explicit','m2','from side, side view, he kneels on the table with his hips raised, his face on the pad, anal speculum, gaping anus, visible inside, she holds the speculum dial, erection, precum',s('SHIORI','slowly widens the anal speculum with a dial','kneels on the table with his hips raised'))
woman_scene('Lab_atk_m3','SHIORI','explicit','m3','from side, he sits in the white chair, thin electrode wire running under him, she presses a button on the control box, electric sparks effect, arched back, toes curled, erection',s('SHIORI','presses the button on the control box','jolts in the chair from the electric stimulation'))
woman_scene('Lab_atk_e1','MINASE','explicit','m1','he reclines on the chair, small transparent sensor patches on both nipples, she taps his nipple with a metal stylus, tablet showing waveform graph, erect nipples',s('MINASE','taps the sensor on his nipple with a stylus','reclines on the chair'))
woman_scene('Lab_atk_e2','CHLOE','explicit','e2','he lies on his back on the padded table, leather straps on his wrists, elbows, knees, waist and chest, she tightens a strap, large headphones on his head, spread legs',s('CHLOE','tightens the leather straps','is strapped down on the table'))
woman_scene('Lab_atk_e3','HAKU','explicit','e3','from side, side view, he kneels on the table with his hips raised, anal speculum, gaping anus, visible inside, she holds the dial and grins, clipboard under her arm, erection',s('HAKU','widens the speculum with a grin','kneels with his hips raised'))
boss_scene('Lab_atk_boss','explicit','boss','the machine lifts him with robotic arms, arms holding his wrists and ankles, suction cup arm on his chest, thin rod arm under him, many arms touching his body, erection, arched back','The large white prototype machine holds the small slim naked man in the air with many robotic arms.')
# 魔法・罠
add('Lab_magic_1','SHIORI','safe',f'{CH["SHIORI"]}, solo, pov, holding a blank white card toward viewer, looking at viewer, {ROOM["bg"]}')
add('Lab_magic_2','MINASE','safe',f'{CH["MINASE"]}, solo, pov, holding small transparent sensor patches between her fingers toward viewer, {ROOM["m1"]}')
add('Lab_magic_3','SHIORI','safe',f'{CH["SHIORI"]}, solo, standing in a laboratory as the ceiling lights turn on, rows of machines, from below, {ROOM["m3"]}')
add('Lab_magic_4','SHIORI','safe',f'{CH["SHIORI"]}, solo, looking at a large blueprint of a machine with only lines, {CH["LX01"].replace("no humans, ","")} in the background, {ROOM["boss"]}')
add('Lab_magic_5','SHIORI','safe',f'{CH["SHIORI"]}, solo, pulling a large lever, lights going dark, red emergency lights, smirk, {ROOM["bg"]}')
# 特殊
add('Lab_inochigoi','SHIORI','safe',f'{CH["SHIORI"]}, solo, kneeling on the floor, pov, looking up at viewer, hands clasped, pleading, tears, torn lab coat, slight hidden smile, {ROOM["bg"]}')
onani('Lab_onanie','SHIORI','wait','sitting on the sofa','He masturbates alone on the waiting room sofa while the silver-haired scientist watches from far away.')
woman_scene('Lab_onedari','SHIORI','explicit','m1','pov from above, he kneels on the floor looking up, she holds a small voice recorder near his mouth, open mouth, begging, from above',s('SHIORI','holds a voice recorder to record his request','kneels and begs'))

# 敗北28
DEF=', defeated, exhausted, limp body, cum on stomach, tears of pleasure'
L={
'm1':('SHIORI','m1',[
 ('btl','he reclines on the chair, wrists strapped, transparent suction cups on his swollen nipples, puffy nipples, arched back'+DEF,'keeps the suction cups on his nipples'),
 ('onani','he sits on the sofa, short straps keep his wrists at chest height, he pinches his own nipples, three monitors show him'+DEF,'watches him touch his own nipples'),
 ('inochi','he sits in the chair, his finger presses a big red button on the armrest, suction cups on his nipples'+DEF,'watches him press the button himself'),
 ('onedari','he sits in the chair, three suction devices small medium and large on a cart, open mouth, begging, she holds a tablet'+DEF,'waits for his request with a tablet')],'wait_room_for_onani'),
'm2':('SHIORI','m2',[
 ('btl','from side, side view, he kneels on the table with hips raised, anal speculum fully open, gaping anus, visible inside, trembling legs'+DEF,'holds the speculum open'),
 ('onani','from side, he kneels on a low table, he holds a small button box in his hand, cable connected to the anal speculum, gaping anus'+DEF,'watches him press the button'),
 ('inochi','from side, he lies on his back, legs in stirrups, he holds the long spring handle of the anal speculum with both hands, gaping anus'+DEF,'watches him hold the handle himself'),
 ('onedari','from side, he kneels on the table with hips raised, a wall panel with a row of ten glowing round lamps, anal speculum, gaping anus, open mouth, begging'+DEF,'turns the dial after his request')],None),
'm3':('SHIORI','m3',[
 ('btl','from side, he sits in the white chair, electrode wire under him, she holds a small speaker, toes curled, arched back'+DEF,'plays a beep from the speaker'),
 ('onani','he sits in the chair, thin wristband on his right wrist and ankle band on his left ankle with wires, toes curled, masturbation'+DEF,'watches him move his hand and toes'),
 ('inochi','he sits in the chair, open mouth, speaking, monitors with graphs in front of him, electrode wire under him'+DEF,'listens with a tablet'),
 ('onedari','he sits in the chair, electrode wire under him, she writes in a paper notebook with a pen, a frequency knob on the control box, open mouth, begging'+DEF,'writes down his requests')],None),
'e1':('MINASE','m1',[
 ('btl','he reclines on the chair, transparent sensor patches on both nipples, she presses his nipples with two metal styluses, tablet with waveform'+DEF,'presses the sensors with styluses'),
 ('onani','he sits on the sofa, wrists strapped to the armrests, she sits on a stool in front of him, handjob, her other hand holds a tablet'+DEF,'strokes him and stops at the edge'),
 ('inochi','he reclines on the chair, a sensor patch only on his left nipple, his right nipple untouched and erect, she taps the left sensor with a stylus'+DEF,'touches only his left nipple'),
 ('onedari','he sits on the sofa, she sits on a stool, handjob, she shows him the tablet, open mouth, begging'+DEF,'strokes him while reading numbers')],None),
'e2':('CHLOE','e2',[
 ('btl','he lies strapped on the body-shaped table, straps on wrists elbows knees waist and chest, she brushes his inner thigh with a soft brush, spread legs'+DEF,'brushes his strapped body'),
 ('onani','he sits on the sofa, large headphones on his head, his wrists linked by a short chain in front of his chest, she speaks into a microphone in the background'+DEF,'guides him with her voice'),
 ('inochi','he lies on the body-shaped table fastening the last leather strap on his own wrist, all other straps already fastened, she stands beside and watches'+DEF,'watches him strap himself down'),
 ('onedari','he sits on the sofa, large headphones on his head, open mouth, begging, she holds a microphone'+DEF,'answers his requests into a microphone')],None),
'e3':('HAKU','e3',[
 ('btl','from side, side view, he kneels on the table with hips raised, anal speculum fully open, gaping anus, she stamps a clipboard with a small stamp, thin metal band on his ankle'+DEF,'stamps her clipboard with a grin'),
 ('onani','he sits on the sofa, electrode cushion under him, she sits on the sofa armrest with a remote control, thin metal band on his ankle, masturbation'+DEF,'presses the remote and grins'),
 ('inochi','from side, he kneels on the table with hips raised, a small desk in front of him, he writes on a clipboard with a pen, anal speculum, gaping anus'+DEF,'leans over to read what he writes'),
 ('onedari','he sits on the sofa, electrode cushion under him, she holds a remote near his face, thin metal band on his ankle, open mouth, begging'+DEF,'waits for him to say his number')],None),
}
for hand,(who,room,rows,_) in L.items():
    for route,scene,verb in rows:
        r='wait' if route=='onani' and who not in ('CHLOE',) and hand not in ('e3',) else room
        if route=='onani': r='wait'
        if hand=='m3' and route=='inochi': r='rec'
        woman_scene(f'Lab_lose_{route}_{hand}',who,'explicit',r,scene,s(who,verb,'is left exhausted'))
B=[('btl','he lies inside the open chest cavity of the machine, the cavity lined with soft padding shaped like his body, many small robotic arms touching his whole body, red light on him','The small slim naked man lies inside the open chest of the large white prototype machine.'),
 ('onani','he sits on the sofa, a robotic arm with a transparent suction cup on his chest, a thin rod arm under him, a thin arm gently wrapped around his right wrist, masturbation','The large white prototype machine moves its arms in sync with his hand.'),
 ('inochi','he is held in the air spread-eagle by four robotic arms at his wrists and ankles in front of the red lens, other arms touching his chest and hips, small sparks from the machine','The large white prototype machine holds him spread-eagle in front of its red lens.'),
 ('onedari','he sits on the sofa, a robotic arm with a transparent suction cup on his chest, a thin rod arm under him, open mouth, speaking toward the red lens','He speaks commands to the large white prototype machine.')]
for route,scene,sent in B:
    boss_scene(f'Lab_lose_{route}_boss','explicit','wait' if route in('onani','onedari') else 'boss',scene+DEF,sent)
json.dump({'mod':'Lab','settings':{'width':832,'height':1216,'steps':36,'cfg':4.5,'sampler':'er_sde','scheduler':'simple'},'images':P},
  open('tools/Lab_prompts.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(P))
