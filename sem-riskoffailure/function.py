def calculate_risk_of_failure(lec, lab, supp, can):
    lec_total = 33
    lec_weight = 0.3
    lab_total = 22
    lab_weight = 0.4
    supp_total = 44
    supp_weight = 0.15
    can_total = 50
    can_weight = 0.15

    # Check that inputs are numbers
    if not all(isinstance(i, (int, float)) for i in [lec, lab, supp, can]):
        raise ValueError("All input values must be numbers.")

    # Check that inputs do not exceed totals
    if not all(0 <= i <= j for i, j in zip([lec, lab, supp, can], [lec_total, lab_total, supp_total, can_total])):
        raise ValueError("Input values must not exceed their respective totals.")

    student_engagement_score = (((lec * lec_weight) / lec_total) 
                                + ((lab * lab_weight) / lab_total) 
                                + ((supp * supp_weight) / supp_total) 
                                + ((can * can_weight) / can_total)) * 100

    return student_engagement_score
