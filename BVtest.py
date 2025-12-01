import webview as wv
from collections import Counter


questions = [
                "I feel energized after attending social events.",
                "I prefer deep one-on-one conversations.",
                "I enjoy being the center of attention.",
                "I need time alone to recharge after socializing.",
                "I easily make new friends.",
                "Large parties drain my energy.",
                "I focus on facts and details rather than ideas.",
                "I trust experience more than theories.",
                "I prefer practical subjects.",
                "I often imagine future possibilities.",
                "I notice small changes in my environment.",
                "Routine quickly bores me.",
                "I make decisions based primarily on logic.",
                "I value truth over tact.",
                "I stay calm when others are emotional.",
                "I consider people's feelings before deciding.",
                "I avoid hurting others' feelings.",
                "Harmony is more important than being right.",
                "I like having a structured daily schedule.",
                "Last-minute changes make me uncomfortable.",
                "I finish tasks well before deadlines.",
                "I enjoy spontaneity and flexibility.",
                "I like to keep my options open.",
                "I work in intense bursts followed by breaks."
            ] * 3

# ==============================================================
# 16 Personality Types
# ==============================================================
deep_analysis = {
    "INTJ": {"name": "Architect", "rarity": "2-4%", "strengths": "Strategic • Visionary",
             "weaknesses": "Critical • Distant", "careers": "CEO • Scientist", "famous": "Elon Musk"},
    "INTP": {"name": "Logician", "rarity": "3-5%", "strengths": "Brilliant • Curious", "weaknesses": "Procrastinates",
             "careers": "Researcher", "famous": "Einstein"},
    "ENTJ": {"name": "Commander", "rarity": "2-5%", "strengths": "Leader • Ambitious", "weaknesses": "Dominating",
             "careers": "Executive", "famous": "Steve Jobs"},
    "ENTP": {"name": "Visionary", "rarity": "3-6%", "strengths": "Innovative", "weaknesses": "Scattered",
             "careers": "Entrepreneur", "famous": "Da Vinci"},
    "INFJ": {"name": "Advocate", "rarity": "1-3%", "strengths": "Insightful", "weaknesses": "Perfectionist",
             "careers": "Counselor", "famous": "MLK"},
    "INFP": {"name": "Mediator", "rarity": "4-5%", "strengths": "Creative", "weaknesses": "Sensitive",
             "careers": "Artist", "famous": "Tolkien"},
    "ENFJ": {"name": "Protagonist", "rarity": "2-5%", "strengths": "Charismatic", "weaknesses": "People-pleasing",
             "careers": "Teacher", "famous": "Oprah"},
    "ENFP": {"name": "Campaigner", "rarity": "7-8%", "strengths": "Enthusiastic", "weaknesses": "Disorganized",
             "careers": "Actor", "famous": "Robin Williams"},
    "ISTJ": {"name": "Logistician", "rarity": "11-14%", "strengths": "Reliable", "weaknesses": "Rigid",
             "careers": "Accountant", "famous": "Washington"},
    "ISFJ": {"name": "Defender", "rarity": "12-15%", "strengths": "Loyal • Caring", "weaknesses": "Takes personally",
             "careers": "Nurse", "famous": "Mother Teresa"},
    "ESTJ": {"name": "Executive", "rarity": "8-12%", "strengths": "Decisive", "weaknesses": "Blunt",
             "careers": "Manager", "famous": "Dr. Dre"},
    "ESFJ": {"name": "Consul", "rarity": "10-13%", "strengths": "Warm", "weaknesses": "Needs approval",
             "careers": "Event Planner", "famous": "Taylor Swift"},
    "ISTP": {"name": "Virtuoso", "rarity": "5-7%", "strengths": "Calm • Practical", "weaknesses": "Reserved",
             "careers": "Surgeon", "famous": "Jordan"},
    "ISFP": {"name": "Adventurer", "rarity": "7-9%", "strengths": "Artistic", "weaknesses": "Poor planning",
             "careers": "Designer", "famous": "Diana"},
    "ESTP": {"name": "Entrepreneur", "rarity": "4-7%", "strengths": "Bold", "weaknesses": "Impulsive",
             "careers": "Sales", "famous": "Madonna"},
    "ESFP": {"name": "Entertainer", "rarity": "7-10%", "strengths": "Fun-loving", "weaknesses": "Avoids planning",
             "careers": "Performer", "famous": "Adele"}
}



def calculate_result(answers):
    traits = []
    for i, ans in enumerate(answers):
        q = i % 20
        if q in [0, 2, 4]:
            traits.append("E" if ans else "I")
        elif q in [1, 3, 5]:
            traits.append("I" if ans else "E")
        elif q in [6, 8, 10]:
            traits.append("S" if ans else "N")
        elif q in [7, 9, 11]:
            traits.append("N" if ans else "S")
        elif q in [12, 14]:
            traits.append("T" if ans else "F")
        elif q in [13, 15]:
            traits.append("F" if ans else "T")
        elif q in [16, 18]:
            traits.append("J" if ans else "P")
        elif q in [17, 19]:
            traits.append("P" if ans else "J")

    c = Counter(traits)
    e_pct = round(100 * c["E"] / max(c["E"] + c["I"], 1))
    n_pct = round(100 * c["N"] / max(c["N"] + c["S"], 1))
    t_pct = round(100 * c["T"] / max(c["T"] + c["F"], 1))
    j_pct = round(100 * c["J"] / max(c["J"] + c["P"], 1))

    ptype = ("E" if e_pct > 50 else "I") + ("N" if n_pct > 50 else "S") + ("T" if t_pct > 50 else "F") + (
        "J" if j_pct > 50 else "P")
    data = deep_analysis.get(ptype, deep_analysis["INTJ"])

    return {
        "type": ptype,
        "percentages": f"E/I: {e_pct}%/{100 - e_pct}% • S/N: {100 - n_pct}%/{n_pct}% • T/F: {t_pct}%/{100 - t_pct}% • J/P: {j_pct}%/{100 - j_pct}%",
        "name": data["name"],
        "rarity": data["rarity"],
        "strengths": data["strengths"],
        "weaknesses": data["weaknesses"],
        "careers": data["careers"],
        "famous": data["famous"]
    }



html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Deep Personality Test</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
  body {font-family:'Inter',sans-serif;background:#0d1117;color:white;margin:0;padding:30px;text-align:center;}
  .c{max-width:900px;margin:0 auto;}
  h1{font-size:48px;background:linear-gradient(90deg,#58a6ff,#1f6feb);-webkit-background-clip:text;color:transparent;}
  .q{font-size:32px;line-height:1.5;margin:80px 0;}
  button{width:300px;height:100px;margin:30px;font-size:34px;border:none;border-radius:20px;cursor:pointer;
         box-shadow:0 12px 30px rgba(0,0,0,0.6);transition:0.3s;}
  .yes{background:#238636;}.yes:hover{background:#2ea043;transform:scale(1.08);}
  .no{background:#da3633;}.no:hover{background:#f85149;transform:scale(1.08);}
  .progress{height:12px;background:#21262d;border-radius:6px;overflow:hidden;margin:40px auto;width:700px;}
  .fill{height:100%;background:#58a6ff;transition:width 0.7s ease;}
  .box{background:rgba(88,166,255,0.15);padding:30px;border-radius:18px;margin:30px 0;}
</style>
</head>
<body>
<div class="c" id="app">
  <h1>Deep Personality Test</h1>
  <p style="color:#8b949e;font-size:22px;">60 Questions • Ultra Accurate • Instant Results</p>
  <button class="yes" id="startBtn">Start Test</button>
</div>

<script>
let answers = [];
let current = 0;
const questions = """ + str(questions) + """;

document.getElementById('startBtn').onclick = function() {
  answers = []; current = 0;
  showQuestion();
};

function showQuestion() {
  const progress = (current + 1) / questions.length * 100;
  document.getElementById('app').innerHTML = `
    <h1>Question ${current+1} <small style="font-size:26px;color:#666">/ 60</small></h1>
    <div class="progress"><div class="fill" style="width:${progress}%"></div></div>
    <div class="q">${questions[current]}</div>
    <button class="yes" onclick="answer(true)">YES</button>
    <button class="no" onclick="answer(false)">NO</button>
  `;
}

function answer(choice) {
  answers.push(choice);
  current++;
  if (current < questions.length) {
    setTimeout(showQuestion, 300);
  } else {
    pywebview.api.get_result(answers);
  }
}

function show_result(data) {
  document.getElementById('app').innerHTML = `
    <h1>Your Personality Type</h1>
    <h2 style="font-size:130px;margin:40px 0;letter-spacing:-6px;">${data.type}</h2>
    <h3 style="color:#58a6ff;font-size:46px;">${data.name}</h3>
    <p style="color:#8b949e;font-size:20px;">Rarity: ${data.rarity}</p>
    <div class="box"><strong>Percentages</strong><br><span style="color:#58a6ff;font-size:26px;">${data.percentages}</span></div>
    <div class="box"><strong>Strengths</strong><br>${data.strengths}</div>
    <div class="box"><strong>Weaknesses</strong><br>${data.weaknesses}</div>
    <div class="box"><strong>Best Careers</strong><br>${data.careers}</div>
    <div class="box"><strong>Famous People</strong><br>${data.famous}</div>
    <button class="yes" style="margin-top:60px;" id="startBtn">Take Again</button>
  `;
  document.getElementById('startBtn').onclick = () => { answers = []; current = 0; showQuestion(); };
}
</script>
</body>
</html>"""


# ==============================================================
# API
# ==============================================================
class Api:
    def get_result(self, answers):
        result = calculate_result(answers)
        wv.windows[0].evaluate_js(f"show_result({result})")


# ==============================================================
# Launch
# ==============================================================
if __name__ == '__main__':
    wv.create_window(
        title="Deep Personality Test",
        html=html,
        width=1100,
        height=800,
        resizable=False,
        js_api=Api(),
        background_color='#0d1117'
    )
    wv.start()