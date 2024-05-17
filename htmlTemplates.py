css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="Icon for this message
user.jpeg
You sentToday at 13:50
https://drive.google.com/file/d/1y8vcU3XpeUo2pbM8HHVr7Hs1fAZz965c/view?usp=drive_link" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://drive.google.com/file/d/18H8mI1tc3zW0OulFdmP3RMRbkp47ZAwI/view?usp=drive_link">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''