# Needs git installed to run this

echo -n "Enter the message for commit: "
read message

git add .
git commit -m "$message" 
git push