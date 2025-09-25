from app import app, db, Message

with app.app_context():
    # Check if messages exist
    count = Message.query.count()
    print(f"Current message count: {count}")
    
    if count == 0:
        # Add test messages
        messages = [
            Message(body="Hello 👋", username="Liza"),
            Message(body="Hi there!", username="Developers"),
            Message(body="How are you?", username="Liza"),
        ]
        
        db.session.add_all(messages)
        db.session.commit()
        print("✅ Test data added!")
    else:
        print("✅ Data already exists!")
    
    # Verify
    messages = Message.query.all()
    for msg in messages:
        print(f"- {msg.body} by {msg.username}")
