# music_agents_abc
The repo demonstrate how to use multi-agents for music generation/arrangements. User can provide prompt and the melody line, and the music agents will help come out with a full song arrangement with harmony and instrumentation covered.    

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

## Reference

Deng, Qixin, et al. "ComposerX: Multi-Agent Symbolic Music Composition with LLMs." arXiv preprint arXiv:2404.18081 (2024).    

Wu, Qingyun, et al. "Autogen: Enabling next-gen llm applications via multi-agent conversation framework." arXiv preprint arXiv:2308.08155 (2023).    