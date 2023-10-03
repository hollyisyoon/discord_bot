import streamlit as st
import feedparser

def check_new_posts(blog_username):
    MEDIUM_RSS_URL = f'https://medium.com/@{blog_username}/latest?format=rss'
    feed = feedparser.parse(MEDIUM_RSS_URL)
    return feed.entries

def main():
    st.title("미디엄 블로그 알림 시스템")
    blog_username = st.text_input("미디엄 블로그 사용자 이름을 입력하세요:")

    if st.button("확인"):
        entries = check_new_posts(blog_username)
        for entry in entries:
            st.write(f"제목: {entry.title}")
            st.write(f"요약: {entry.description}")
            st.write(f"링크: {entry.link}")
            st.write("---")

if __name__ == "__main__":
    main()
