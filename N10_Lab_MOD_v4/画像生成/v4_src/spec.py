PAIR = "1girl, 1boy, cfnm, femdom, hetero"
PRON = "her"
PRON_SUBJ = "she"
SOLO = "1girl"
PLACE = "abandoned research laboratory, long white corridor, cracked windows, pale fluorescent lights, old monitors, cables on the floor"
def _adult(age):
    return f"mature female, adult woman, {age} years old, mature face, adult proportions, long legs"
ADULT = _adult(25)
CHARS = {
 "master": dict(phrase="the silver-haired woman wearing a white lab coat", outfit="white lab coat",
                tags=_adult(31) + ", silver hair, short messy hair, red eyes, goggles on forehead, white lab coat, black turtleneck sweater, latex gloves, medium breasts, cold expressionless face, scientist"),
 "e1": dict(phrase="the light gray-haired woman wearing a lab coat over a gray blouse", outfit="lab coat over a gray blouse",
            tags=_adult(25) + ", light gray hair, bob cut, light blue eyes, white lab coat, gray blouse, holding a tablet, small breasts, expressionless, flat gaze"),
 "e2": dict(phrase="the dark blue-purple-haired woman wearing a lab coat and black gloves", outfit="lab coat and black gloves",
            tags=_adult(27) + ", dark blue-purple hair, short hair, purple eyes, white lab coat, black gloves, leather belt at waist, medium breasts, calm neutral expression"),
 "e3": dict(phrase="the white-haired woman wearing a lab coat with rolled-up sleeves", outfit="lab coat with rolled-up sleeves",
            tags=_adult(24) + ", white hair, high ponytail, green eyes, white lab coat, sleeves rolled up, latex gloves, clipboard, medium breasts, playful grin"),
 "boss": dict(phrase="the large white prototype machine with a glowing red lens", outfit="white armor plating",
              tags="large mechanical device, no humanoid form, white and gray armor plating, multiple robotic arms, thin finger-like manipulator arms, suction arms, single large glowing red lens, prototype machine, floor-mounted, sci-fi laboratory equipment, 230cm tall",
              pair="1boy, solo male, machine, mechanical arms, femdom machine", solo="no humans, machine", pron="its", pron_subj="it",
              a_suffix="a machine, not a person, no woman, no girl, no human body, towering over him"),
}
