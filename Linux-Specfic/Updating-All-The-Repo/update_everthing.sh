# A script to update every repo in the directory

for entry in `ls $search_dir` 
do
    if [[ -d $entry ]] 
    then
        cd $entry
        git pull
        cd ..
    fi
done
