import requests
import json
import subprocess
from configs import conf as _c


def get_git_diff_files():
  res= subprocess.run(['git', 'diff', '--name-only'], capture_output=True, text=True)
  return res.stdout.strip().split('\n')

def analyze_diff():
  files= get_git_diff_files()

  for file_name in files:
    if file_name in _c.SKIP_FILES: continue
    with open(file_name, "r", encoding="utf-8") as f: code = f.read()
    res_diff= subprocess.run(['git', 'diff', file_name], capture_output=True, text=True)
    diff= res_diff.stdout.strip()

    print(f"📖 [{file_name}] LLM Review in progress...")
    
    prompt= f"You're an expert Developer. Rewiew the diff of this file: \n\nCODE: {code} \n\nDIFF: {diff}"
    _c.LLM_DATA['prompt']= prompt
    try:
      response= requests.post(_c.OLLAMA_SERVER, json= _c.LLM_DATA)
      jres= response.json()['response']
      print(f"🤖 [{file_name}] LLM Review done:\n\n")
      llm_res_file= f"diff_{file_name}.txt"
      with open(llm_res_file, "w") as f: f.write(jres)
      print(f"💾 [{file_name}] LLM Answer saved to: {llm_res_file}")
    except Exception as e:
      print(f"❌ Error during file analyze: {file_name} {e}")

if __name__ == "__main__":
  analyze_diff()
