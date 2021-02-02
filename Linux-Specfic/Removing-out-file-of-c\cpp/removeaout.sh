t_p() {
    for entry in `ls $search_dir` 
    do 
        if [[ "$entry" == "a.out" ]];  
        then 
            rm a.out
            echo "Removing"
        elif [[ -d $entry ]];
        then 
            cd $entry
            t_p
            cd ..
        fi  
    done
}

t_p