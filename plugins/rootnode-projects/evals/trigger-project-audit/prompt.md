---
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

I run a Claude Project for our customer support team and the answers have been getting worse. Can you score how it's set up and tell me what to fix first?

Custom Instructions:
You are a helpful assistant for Northwind Support. Be friendly and professional. Answer customer questions using the knowledge files. Always be accurate. Keep answers short but also include all relevant detail. If you don't know, say so. Follow the refund policy. Use our brand voice. Escalate angry customers.

Knowledge files:
- refund-policy-2023.pdf
- refund-policy-2025-final.pdf
- brand-voice.docx
- everything-about-our-products.txt (about 200 pages)
- old-chat-exports.txt
