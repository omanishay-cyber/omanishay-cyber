"""Writes ../../README.md. One paragraph per line: GitHub's renderer turns single newlines into line breaks."""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PERCH = 'https://github.com/omanishay-cyber/perch'
PERCH_SITE = 'https://omanishay-cyber.github.io/perch/'
PERCH_DL = 'https://github.com/omanishay-cyber/perch/releases/latest/download/Perch-Setup.exe'
STRYX = 'https://github.com/omanishay-cyber/stryx-skills'
STRYX_SITE = 'https://skills.stryxlabs.com/'
STRYX_PAGE = 'https://omanishay-cyber.github.io/stryx-skills/'
LABS = 'https://stryxlabs.com'
MNEME = 'https://github.com/omanishay-cyber/mneme'
MNEME_SITE = 'https://mneme.stryxlabs.com'


def pic(name, alt, href=None):
    """A light and dark pair, full width."""
    tag = (f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/{name}-dark.webp">'
           f'<source media="(prefers-color-scheme: light)" srcset="assets/{name}-light.webp">'
           f'<img src="assets/{name}-dark.webp" alt="{alt}" width="100%"></picture>')
    return f'<a href="{href}">{tag}</a>' if href else tag


def one(name, alt, href=None):
    """One picture for both themes, full width."""
    tag = f'<img src="assets/{name}.webp" alt="{alt}" width="100%">'
    return f'<a href="{href}">{tag}</a>' if href else tag


def chapter(anchor, name, alt):
    return f'<a name="{anchor}"></a>\n\n<h3>{pic(name, alt)}</h3>'


def btn(name, alt, href, w=270):
    return f'<a href="{href}"><img src="assets/{name}.webp" alt="{alt}" width="{w}"></a>'


P = []
add = P.append

add('<p>' + pic('banner', 'Anish Trivedi. DevOps and AI developer, graphic designer, New Jersey. Three works: Perch, Stryx Skills and Mneme Genesis. A still mountain lake at night, one lit tree far off.') + '</p>')
add('<p align="center"><a href="#perch"><b>Perch</b></a> &nbsp;·&nbsp; <a href="#stryx"><b>Stryx Skills</b></a> &nbsp;·&nbsp; <a href="#mneme"><b>Mneme</b></a> &nbsp;·&nbsp; <a href="#workshop">The workshop</a> &nbsp;·&nbsp; <a href="#try">Try one</a></p>')
add('I build the software you look at all day, and the AI tools that run on your own machine. I write the code, run the servers and draw the pictures, so the thing you install and the page that sold it to you come from the same hands. Three of those things are below. All three are free to use.')

# ---------- Perch
add(chapter('perch', 'ch1', 'Chapter one: Perch, a new shell for Windows.'))
add('<p>' + pic('perch-cover', 'Perch: the Windows taskbar, reconsidered. The real notch open at the top of the screen and the real dock at the bottom, over a mountain lake.', PERCH_SITE) + '</p>')
add('**You look at the same strip of icons all day. Perch makes it worth looking at.** The taskbar becomes a dock whose icons grow under your pointer. The empty top of your screen becomes a notch with the time, the weather, your music and how your PC is doing. The Start button opens a menu you pick from twelve designs. Your apps, files and settings stay exactly where they are, and if you ever remove Perch the Windows taskbar comes straight back.')
add('<p>' + pic('perch-nums', 'Perch in numbers: 12 notch designs, 12 Start menu designs in 21 flavors, 3 dock styles, 10 colour palettes, 2 looks called Simple and Graphics, and it costs 0 dollars at home or at work.') + '</p>')
add('<p>' + one('perch-start', 'Twelve Start menu designs, twenty-one flavors in all, one click each. All twelve fanned out as a stack of cards.', PERCH_SITE) + '</p>')
add('**A Start menu that does more than start things.** Type `12*7` and the answer is the top result. Type `10 km to mi` and it converts. It finds Windows Settings pages by the words people actually use, works as a Run box, and learns which apps you open at this hour.')
add('<p>' + pic('perch-notch', 'The notch: everything, one hover up. The calendar and timer panel hanging from the top of the screen over a misty forest.', PERCH_SITE) + '</p>')
add('**A notch with a job.** Twelve live numbers from CPU to battery, a full music player with five visualizers and live lyrics, Wi-Fi and Bluetooth without opening Settings, a volume for every app, a clipboard you can read, a shelf for your files. It steps aside over full-screen games and can leave a tiny CPU, GPU and RAM strip instead.')
add('<p>' + pic('perch-dock', 'The dock: the taskbar, grown up. The real dock over a coastal dusk, with live previews of two Edge windows.', PERCH_SITE) + '</p>')
add('<p>' + pic('perch-mosaic', 'Five real Perch screens: a timer that draws itself round the notch, icons that grow under your pointer, your song at the top of the screen, search that does the sum, and a volume for every app.') + '</p>')
add('<details><summary><b>Everything else in the box</b></summary>\n\n<ul><li><b>Privacy dots:</b> orange while an app uses the microphone, green for the camera. Point at one to see which app.</li><li><b>Power menu with a safety catch:</b> Restart and Shut down ask for a second click.</li><li><b>Dock extras:</b> drives, special folders, any folder you add, the Recycle Bin, Win+1 to Win+9, unread badges.</li><li><b>Start menu:</b> jump lists, pinned folders, a letter grid, a widgets strip, full keyboard control.</li><li><b>Looks:</b> your own colour, five spring feels, light and dark that follow Windows.</li><li><b>Updates:</b> signed. Perch refuses any update whose signature does not match. Turn Auto update off and nothing changes without you.</li><li><b>Runs on:</b> Windows 11 and Windows 10 version 22H2, on every screen size and scaling level, touch screens too.</li></ul>\n\n</details>')
add('<p>' + btn('btn-perch', 'Download Perch for Windows', PERCH_DL) + '</p>')
add(f'[Website]({PERCH_SITE}) &nbsp;·&nbsp; [Repository and release notes]({PERCH}) &nbsp;·&nbsp; Free, at home or at work')

# ---------- Stryx
add(chapter('stryx', 'ch2', 'Chapter two: Stryx Skills, a lab for Claude Code.'))
add('<p>' + pic('stryx-hero', 'Stryx Skills for Claude Code: the lab\'s methods, grown into one tree. 94 skills in eight groups, 32 agents, 46 hook files, 62 design laws, 52 ready ops. A tree of coloured light on a still lake.', STRYX_SITE) + '</p>')
add('**An AI coder is only as good as its habits.** Left alone it works from memory, skips the check and tells you it is done. Stryx Skills gives Claude Code 94 skills and 32 agents, each written for one kind of work. A router reads your request and loads the right ones before Claude starts, and nothing counts as done until a check proves it.')
add('<p>' + pic('stryx-f1', 'The router fans one request out to the debug, react and verify skills. The hooks block a delete, find a leaked key and refuse a done with no proof.') + '</p>')
add('<p>' + pic('stryx-f2', 'Designs are held to 62 laws with 52 ready ops for glass, metal, water, sky and light. Your own graphics card goes first through Ollama, LM Studio and ComfyUI.') + '</p>')
add('<p>' + pic('stryx-f3', 'One word steers Claude: coldstart holds, hotstart goes one task at a time, firestart loads the mission\'s skills. 32 agents work in the background while the chat stays free.') + '</p>')
add('<p>' + pic('stryx-flow', 'From request to proven done, in five steps: your request, the router, the skills, the checks, then done with evidence.') + '</p>')
add('<details><summary><b>Without it, and with it</b></summary>\n\n<ul><li><b>Without:</b> you name the method each time. <b>With:</b> the router loads the matching skills before Claude starts.</li><li><b>Without:</b> "done" means Claude said so. <b>With:</b> the stop judge wants test output, a type check or a screenshot.</li><li><b>Without:</b> one wrong command can delete a folder. <b>With:</b> the guard blocks it before it runs.</li><li><b>Without:</b> a key can slip into a commit. <b>With:</b> the secret scanner looks for keys and passwords.</li><li><b>Without:</b> designs drift to the same generic look. <b>With:</b> 62 laws, 52 ops and a design detector.</li><li><b>Without:</b> a long job blocks the chat. <b>With:</b> 32 agents take big jobs in the background.</li></ul>\n\n</details>')
add('```powershell\nirm https://skills.stryxlabs.com/install.ps1 | iex\n```')
add('<p>' + btn('btn-stryx', 'Get Stryx Skills', STRYX_SITE) + '</p>')
add(f'[Product page]({STRYX_SITE}) &nbsp;·&nbsp; [GitHub page]({STRYX_PAGE}) &nbsp;·&nbsp; [Repository]({STRYX}) &nbsp;·&nbsp; [Stryx Labs]({LABS}) &nbsp;·&nbsp; Windows. No fee, no subscription, no key, no sign-up.')

# ---------- Mneme
add(chapter('mneme', 'ch3', 'Chapter three: Mneme Genesis, memory for AI coding.'))
add('<p>' + pic('mneme-cover', 'Mneme Genesis. Where the memory begins. 49 tools, 11 scanners, 14 WebGL views, 100 percent local. Star trails over a still lake, with one recall path lit among them.', MNEME_SITE) + '</p>')
add('**Your AI forgets your project every time the chat ends. Mneme keeps it.** Mneme is a local memory and code graph for AI coding tools. It keeps the graph current as you save and holds what was learned on your own disk, so the next session starts where the last one stopped.')
add('<p>' + pic('mneme-cold', 'A new chat does not start cold. You work and it keeps a graph of your code, current as you save. The chat compacts and the details stay in a store on your disk. The next chat picks up where the last one ended.') + '</p>')
add('<p>' + pic('mneme-ask', 'Ask it what you would ask a colleague. Recall: where is the auth handler? Blast radius: what breaks if I change this? Call graph: who calls it? Decision: why did we build it this way? Constraint: what must stay true? To-do: what is left to do?') + '</p>')
add('```bash\n# macOS and Linux\ncurl -fsSL https://stryxlabs.com/install.sh | bash\n```')
add('```powershell\n# Windows (PowerShell)\niex (iwr https://stryxlabs.com/install.ps1).Content\n```')
add('Both scripts detect your platform, verify SHA-256 checksums and install to `~/.mneme`. Free on your own code, personal or commercial. The source is closed.')
add('<p>' + btn('btn-mneme', 'Install Mneme', MNEME_SITE) + '</p>')
add(f'[Docs and install guide]({MNEME_SITE}) &nbsp;·&nbsp; [Repository]({MNEME})')

# ---------- Workshop
add(chapter('workshop', 'ch4', 'Chapter four: the workshop, what I do and with what.'))
add('<p>' + pic('craft', 'The workbench. Systems and DevOps: Rust, Tokio, SQLite, tree-sitter, supervisors, watchdogs, signed updates, release pipelines on GitHub Actions. Desktop and web: TypeScript, React, Svelte, Electron, Tauri, Bun. AI tooling: MCP, Claude Code, ONNX, fastembed, and Ollama, LM Studio and ComfyUI on my own GPU. Graphic design: type, colour in OKLCH, icons, motion, every picture on this page.') + '</p>')
add('**What I believe about software**')
add('1. Start from the user\'s pain, not from the tech stack. Every feature should answer a problem you can say in one sentence.\n2. Stay local-first until you have a reason not to.\n3. An AI forgetting your project is an architecture problem, not a prompt problem. Store the memory outside the chat.\n4. Write the README before the code. If you can\'t explain it plainly, it isn\'t designed yet.\n5. Ship small and often. Something people use today beats a perfect plan that never ships.')

# ---------- CTA
add(chapter('try', 'ch5', 'Chapter five: your turn, try one tonight.'))
add('<p>' + pic('closing', 'All three are free. Pick one and try it tonight. A small bird on a bare branch at first light.') + '</p>')
add('<p align="center">' + ' '.join([btn('btn-perch', 'Download Perch for Windows', PERCH_DL), btn('btn-stryx', 'Get Stryx Skills', STRYX_SITE), btn('btn-mneme', 'Install Mneme', MNEME_SITE)]) + '</p>')
add(f'Want to talk about local-first AI tools, MCP servers, Claude Code or desktop app design? Write to [hello@stryxlabs.com](mailto:hello@stryxlabs.com), or see the rest of the lab at [stryxlabs.com]({LABS}).')
add('<sub>New Jersey, USA · BS in Computer Science · The paintings on this page came from a model on my own GPU. The screens are the real apps with made-up data.</sub>')

with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n\n'.join(P) + '\n')
print('README written', sum(len(x) for x in P))
