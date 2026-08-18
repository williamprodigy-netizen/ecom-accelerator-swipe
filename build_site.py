#!/usr/bin/env python3
"""Build the Ecom Accelerator swipe site. Run: python3 build_site.py"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/ECOM_ACCELERATOR_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/**/*.mp4"), recursive=True)):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(os.path.basename(p), "")))
    return rows


ROLES = {'EcomAccelerator_VSL.mp4': 'The chaptered TikTok Shop VSL, served by Vidalytics.'}

CONFIG = {
 "SITE": "Ecom Accelerator — TikTok Shop DFY",
 "CREATOR": "Ecom Accelerator",
 "ADS_KEY": "ecomaccelerator",
 "FUNNEL_IDS": ["F048"],
 "CAPTURED": "18 August 2026",
 "REPO": REPO,
 "PACKAGE": "~/Downloads/Swipes/ECOM_ACCELERATOR_Swipe",
 "BLURB": "Done-for-you TikTok Shop stores, live in 31 days, behind a &ldquo;no profit&rdquo; "
          "guarantee. The VSL is <b>chaptered</b> &mdash; the viewer can jump to the proof.",
 "PAGES": [("index.html","Overview"),("analysis.html","Analysis"),
              ("transcripts.html","Transcripts"),("videos.html","Video library")],
 "STATS": [("Vehicle","TikTok Shop"),("Model","Done-for-you store"),("VSL","4m 49s"),
           ("Words","982"),("Speed claim","Live in as little as 31 days"),
           ("Player","Vidalytics (chaptered)"),("Application","Typeform"),("Price","never stated")],
 "OFFER": [("Product","&ldquo;We <b>build &amp; manage</b> your ecommerce business &mdash; live in as little as 31 days&rdquo;"),
   ("Vehicle","TikTok Shop, positioned as &ldquo;Amazon's new rival&rdquo; per the Wall Street Journal"),
   ("Market proof","&ldquo;A billion users&hellip; 50 times larger than Amazon's user base in 2000&hellip; 90 minutes per day&rdquo;"),
   ("Guarantee","A <b>&lsquo;No Profit&rsquo; guarantee</b>, gated on qualifying"),
   ("Path","VSL (chaptered) &rarr; Typeform application &rarr; booked strategy call &rarr; confirm-your-call video"),
   ("Price","<b>Never stated</b>")],
 "FINDINGS": [
  ("The VSL has chapter navigation &mdash; unusual, and worth testing",
   "The player exposes jump links: <b>&ldquo;The Hidden Cash Flow Opportunity&rdquo;</b>, "
   "<b>&ldquo;Why TikTok Shop Is Different&rdquo;</b>, <b>&ldquo;Proof From the Trenches&rdquo;</b>. "
   "Almost every VSL in this file is a locked linear argument; this one lets a sceptic skip "
   "straight to the proof. It trades control of the argument for respect of the viewer's time "
   "&mdash; the opposite bet to the forced-consumption players (Warrior Babe, Brook Hiddink)."),
  ("The whole opening is borrowed authority about a platform, not about them",
   "&ldquo;Top economists from the <b>Wall Street Journal</b> are referring to this platform as "
   "Amazon's new rival.&rdquo; The first 60 seconds sell <i>TikTok Shop</i>, not Ecom Accelerator. "
   "You cannot be sceptical of the seller while you are still deciding about the market. "
   "<b>Sell the wave before you sell the surfboard.</b>"),
  ("The 2000-Amazon comparison does the maths for you",
   "&ldquo;A billion users &mdash; that's <b>50 times larger</b> than Amazon's user base in "
   "2000.&rdquo; It invites the prospect to imagine having bought Amazon in 2000 without ever "
   "making the claim. Regret-avoidance framing, no promise attached, nothing to disprove."),
  ("Confirming the call is a separate, named step",
   "The thank-you page is a numbered checklist: <b>Step 1</b> add to calendar, <b>Step 2</b> watch "
   "the short video <i>to confirm your call</i>. Watching is framed as the confirmation action. "
   "Fifth competitor in this file putting work between booking and attending."),
 ],
 "FUNNEL": [
  ("VSL + application","go.ecomaccelerator.io/fb/vsl",'<span class="tag good">chaptered VSL</span> Vidalytics player with jump links. Typeform application embedded. Meta Pixel.'),
  ("Thank-you / booked","go.ecomaccelerator.io/fb/thank-you","&ldquo;CONGRATS! Your strategy call is booked.&rdquo; Step 1 calendar, Step 2 confirm-by-watching. 15 client videos."),
 ],
 "TRANSCRIPT_GROUPS": [("Ecom Accelerator VSL",[os.path.join(PKG,"Transcript/transcript.md")])],
 "SLIDE_PAGES": [],
 "ANALYSIS": """
<div class="note"><b>A chaptered VSL is the contrarian bet in this file.</b> Everyone else forces
consumption. This one hands the sceptic a shortcut to &ldquo;Proof From the Trenches&rdquo; and
bets that a fast yes beats a captive maybe.</div>

<h2 class="sec">Forced consumption vs. let-them-skip</h2>
<div class="tablewrap"><table>
<tr><th>Who</th><th>Player behaviour</th><th>The bet</th></tr>
<tr><td>Warrior Babe</td><td>Forced consumption, apply unlocks later</td><td>Time invested creates commitment</td></tr>
<tr><td>Brook Hiddink</td><td>Forced-consumption opt-in before the application</td><td>Same</td></tr>
<tr><td><b>Ecom Accelerator</b></td><td><b>Chapter jump links</b></td><td><b>Let the sceptic self-serve the proof</b></td></tr>
</table></div>
<p style="margin-top:12px"><span class="tag">READ</span> Worth a real test on our replay page.
The people who skip to proof are not the people who were going to sit through 90 minutes anyway,
and right now we lose them entirely.</p>

<h2 class="sec">The opening sells the market, not the offer</h2>
<p>982 words is a short VSL, and roughly the first quarter of it never mentions the product. It
establishes TikTok Shop as an inevitability using third-party authority (WSJ), scale (a billion
users), engagement (90 minutes a day) and a regret analogy (Amazon in 2000). Only then does the
DFY offer arrive.</p>
<p>This is the &ldquo;new opportunity&rdquo; structure done cleanly. The prospect's scepticism is
spent on the <i>platform</i>, and by the time the offer appears there is none left over for it.</p>

<h2 class="sec">The stack</h2>
<p><b>DropFunnels</b> on WordPress multisite, <b>Vidalytics</b> for the player, <b>Typeform</b> for
the application, <b>Hyros</b>, Meta Pixel, and two separate GTM containers &mdash; one of them
first-party on <code>load.st.ecomaccelerator.io</code>, which is a deliberate ad-blocker dodge.</p>

<h2 class="sec">What is missing</h2>
<ul><li><b>No price</b>, and the &ldquo;No Profit&rdquo; guarantee is cut off mid-heading on the page &mdash; its full terms were never visible.</li>
<li><b>No emails</b> &mdash; opt-in never submitted.</li>
<li><b>The 15 thank-you client videos are catalogued but not pulled.</b></li></ul>
""",
}
CONFIG["VIDEOS"] = video_library()

if __name__ == "__main__":
    build(CONFIG)
