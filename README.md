# Python-Post-Renewal-Automation-Program
Script for renewing advertisement and vacancies posts on Yeeyi.com with **Python 3** and **Selenium**. Automate the process of updating your posts in less than 100 lines.

# Background
Yeeyi.com is one of Australia's largest comprehensive Chinese online portal and community interactive platforms. It is committed to building an online platform that provides a pleasant interactive experience for Chinese people living in Australia. My family business posts recruitment advertisements on Yeeyi.com when there are vacancies in the company. The process of posting, maintaining and updating (aka thread-lifting in the context of Yeeyi, which refers to raising the popularity of a post for more people to see by updating it) is quite repetitive and therefore replaceable by the code in this script.

# Customisation
To use this script for your own Yeeyi.com posts, you need to fill out the lines located near the start of the script, under the comment `TO BE FILLED BY USER`. The fields are personal account details such as username, password, and the keywords in the type of posts you'd like to  update. Each line should be rather self-explanatory, but do contact me if there are any confusions.

# Comments
One way to 'lift-thread' in Yeeyi.com is by commenting on the post. The comments used in this script is **randomly** drawn from a text file called `comments.txt`, which you need to create yourself. Simply add a file called `comments.txt` and place a suitable comment **on each new line**.

# Skills Involved
- Python
- Selenium
- Web crawling 
- Basic maths (dividing the 15 chances of thread-lifting among the to-update posts, and automatically wait for 120 seconds before updating the next post as required by Yeeyi's policy)

