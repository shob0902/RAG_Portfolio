from flask import Flask, request, jsonify
from flask_cors import CORS
from rag.chain import RAGChain
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5500", "http://127.0.0.1:5500", "http://localhost:8000", "http://127.0.0.1:8000", "http://localhost:3000", "http://127.0.0.1:3000", "https://shob0902.github.io/RAG_Portfolio/", "null"]}})
chatbot = RAGChain()
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "service": "Portfolio AI Backend"
    })
@app.route("/api/chat", methods=["GET","POST"])
def chat():
    if request.method == "GET":
        return jsonify({
            "message": "Use POST to interact with this endpoint."
        })
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON body provided."
            }), 400
        question = data.get("message", "").strip()
        if not question:
            return jsonify({
                "success": False,
                "message": "Message cannot be empty."
            }), 400
        system_prompt = data.get("system_prompt")
        result = chatbot.ask(
            question=question,
            system_prompt=system_prompt
        )
        return jsonify({
            "success": True,
            "answer": result["answer"],
            "sources": result["sources"]
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
@app.route("/api/history", methods=["GET"])
def history():
    history = []
    for message in chatbot.history():
        history.append({
            "type": message.__class__.__name__,
            "content": message.content
        })
    return jsonify(history)
@app.route("/api/clear", methods=["POST"])
def clear():
    chatbot.clear_memory()
    return jsonify({
        "success": True,
        "message": "Conversation cleared."
    })
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
