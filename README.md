# music_agents_abc
The repo demonstrate how to use multi-agents for user-conditioned music arrangements. Multi-agents include a leader, MelodyAgent, HarmonyAgent, InstrumentAgent, ArrangementAgent, and ReviewerAgent.    

User can provide prompt and the melody line, and the music agents will help come out with a full song arrangement with harmony and instrumentation covered.    

Please check the methods with the references below.

## Setup
Please use `requirements.txt` or `env.yml`.   
TBA: abc2midi package    

## Running
Please follow the command:
```
python set_pipe.py -p "path to your JSON file that contains the prompts" -o "directory to store the results"
```
Reference prompt can be seen in `prompt_test_acc.json`.    
TBA: abc format to midi format transformation.    

You can also simply run `python multi_agent_arrangement.py` to see the interations between agents.

## Examples
Prompt and melody line: 
```
Flamenco Test: Compose a fiery flamenco piece with the melody line A4 Bcde | f2 ed cAFA | G4 Bcde | f2 ed cAFA |. Use a classical guitar and piano as the main instrument, and complemented by drums for rhythm. The motif should be passionate and quick, with a progression like Am-G-F-E. Set the tempo fast, with a lot of rhythmic intensity and flair.
```
GPT-3.5 agents output: (in abc notation)
```
X:1
T:Flamenco Test
C:Anonymous
M:4/4
L:1/8
K:Am
V:1 name="Classical Guitar" clef=treble
%%MIDI program 1 24
|:A4 Bcde | f2 ed cAFA | G4 Bcde | f2 ed cAFA:|
V:2 name="Piano" clef=treble
%%MIDI program 2 1
|:(c2E2) (F2A2) (G2B2) (c2e2) | (c2A2) (AGFA) (G2c2) z2 | (G2B2) (AFdA) (G2c2) (B2AG) | (F2D2) (C2E2) C4 z2 :|
V:3 name="Drums" clef=percussion
%%MIDI program 3 118
|:A,,4 EFGA|B,2A,G, G,4|A,,4 EFGA|B,2A,G, G,4:|
V:4 name="Drums" clef=percussion
%%MIDI program 4 118
|:(A,,2c2) (G,,2E2) (F,,2G,2) (E,2F,) | (E,2C) B,4 | (D,2E,) (C,2E) (F,2G,) (A,,2B,) | (C,2D,) C,4 :|
```

GPT-4 agents output: (in abc notation)
```
X:1
T:Flamenco Test
C:Unknown
M:4/4
L:1/8
Q:120
K:Am
V:1 name="Guitar" clef=treble
%%MIDI program 1 24
|:a2e'2 a3b|c'ba2 c'4 | g'2e'2 g'3a|b'ag2 b'4 :|
%%MIDI program 1 24
|:A4 Bcde|f2 ed cAFA|G4 Bcde|f2 ed cAFA:|
V:2 name="Piano" clef=treble
%%MIDI program 2 0
|:c4 A,2E2|G,4 F,4 | E,4 D,2C,2|F,4 E,4 :|
%%MIDI program 2 0
|:C4 A,2E2|G,2A,2 C4|C4 A,2E2|G,2A,2 C4:|
V:3 name="Drums" clef=percussion
%%MIDI program 3 9
|:gggg gggg|gggg gggg|gggg gggg|gggg gggg:|
%%MIDI program 3 9
|:GGGG GGGG|GGGG GGGG|GGGG GGGG|GGGG GGGG:|
```
The user provided melody line will be kept along with new instrumentation and arrangement.

## Reference

Deng, Qixin, et al. "ComposerX: Multi-Agent Symbolic Music Composition with LLMs." arXiv preprint arXiv:2404.18081 (2024).    

Wu, Qingyun, et al. "Autogen: Enabling next-gen llm applications via multi-agent conversation framework." arXiv preprint arXiv:2308.08155 (2023).    