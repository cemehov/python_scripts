def find_top_20(candidates):
    for i in candidates:
        sum_bals = i["scores"]["math"] + i["scores"]["russian_language"] + i["scores"]["computer_science"] + i["extra_scores"]
        i["sum_bals"] = sum_bals

        
    candidates = sorted(candidates, key=lambda student: (student["sum_bals"], student["scores"]["math"], student["scores"]["computer_science"]), reverse=True)
    return [i["name"] for i in candidates[:20]]
    
