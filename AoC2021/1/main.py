with open("data.in") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

    # Worst practices in action <3
    prev1 = 99999
    prev2 = 99999
    prev3 = 99999
    count = 0
    for line in lines:
        if line + prev1 + prev2 > prev1 + prev2 + prev3:
            count = count + 1
        prev3 = prev2
        prev2 = prev1
        prev1 = line
    print(count)
Credinta e un lucru foarte personal. Nu vrei totusi sa-ti pastrezi gandirile habotnice pentru tine? Pe majoritatea nu-i intereseaza :)
Fara credinta omul e nimic? Daca tu faci fapte bune doar de frica unui barbos din cer inseamna ca tu esti un om de nimic. Si nu uita ca atat Romania, cat si Republica Moldova, sunt state seculare prin constitutie, unde ai libertatea sa crezi ce vrei. Exista chiar si in armata o gramada de atei, catolici, protestanti, chiar si musulmani cu origini turcesti din zona dobrogei (cel putin in armata romana). Bine ca vine nimeni in drum  "M.A" sa ii discrediteze pentru ca ei nu cred in balivernele tale...