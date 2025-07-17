from github_activity import get_yesterday_commits
from generate_post import create_post
from linkedin_post import post_to_linkedin
from twitter_post import post_to_twitter
from notify import send_telegram_message
from datetime import datetime

def log_result(status, message):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] [{status}]\n{message}\n\n")

def run_bot():
     
    try:
        updates = get_yesterday_commits()
        if not updates:
            msg = f"🛌 No GitHub activity yesterday. No post made. ({datetime.now().date()})"
            send_telegram_message(msg)
            log_result("SKIPPED", msg)
            return

        post = create_post(updates)
        # post = "Yesterday I improved my portfolio by adding project cards and animations. Check it out: https://github.com/your-username/portfolio-website"
        # Post to LinkedIn
        try:
            post_to_linkedin(post)
            log_result("LINKEDIN_POSTED", post)
        except Exception as e:
            log_result("LINKEDIN_FAILED", str(e))

        # Post to Twitter
        try:
            post_to_twitter(post)
            log_result("TWITTER_POSTED", post)
        except Exception as e:
            log_result("TWITTER_FAILED", str(e))
        


        success_msg = f"✅ Posted successfully:\n\n{post}"
        send_telegram_message(success_msg)
        log_result("SUCCESS", post)

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        send_telegram_message(error_msg)
        log_result("ERROR", error_msg)

if __name__ == "__main__":
    run_bot()
