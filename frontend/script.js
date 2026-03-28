// ================= GLOBAL =================
let selectedLoanType = localStorage.getItem("selectedLoanType") || "";

// ================= HOMEPAGE NAVIGATION =================
const homepage = document.getElementById("homepage");
const lp = document.getElementById("lp"); // loan page
const ip = document.getElementById("ip"); // investment page
const page1 = document.getElementById("page1");
const back1 = document.getElementById("back1");
const startbtn = document.getElementById("startbtn");

lp?.addEventListener("click", () => {
  selectedLoanType = "Education";
  localStorage.setItem("selectedLoanType", selectedLoanType);
  page1.classList.remove("hidden");
  homepage.classList.add("hidden");
});

ip?.addEventListener("click", () => {
  selectedLoanType = "Investment";
  localStorage.setItem("selectedLoanType", selectedLoanType);

  window.location.href = "investment.html";
});


back1?.addEventListener("click", () => {
  page1.classList.add("hidden");
  homepage.classList.remove("hidden");
});

startbtn?.addEventListener("click", () => {
  window.location.href = "step1.html";
});

// ================= EDUCATION =================
const educationAnswers = {
  educationLevel: "",
  collegeTier: "",
  courseNature: "",
  courseFee: "",
  familyIncome: "",
  coApplicant: "",
  coCreditScore: ""
};

document.querySelectorAll("#Q1 .option-card").forEach(btn => {
  btn.addEventListener("click", () => {
    educationAnswers.educationLevel = btn.textContent;
  });
});
document.querySelectorAll("#Q2 .option-card").forEach(btn => {
  btn.addEventListener("click", () => {
    educationAnswers.collegeTier = btn.textContent;
  });
});
document.querySelectorAll("#Q3 .option-card").forEach(btn => {
  btn.addEventListener("click", () => {
    educationAnswers.courseNature = btn.textContent;
  });
});
document.querySelectorAll("#Q6 .option-card").forEach(btn => {
  btn.addEventListener("click", () => {
    educationAnswers.coApplicant = btn.textContent;
  });
});

document.getElementById("courseFee")?.addEventListener("input", e => {
  educationAnswers.courseFee = e.target.value;
});
document.getElementById("familyIncome")?.addEventListener("input", e => {
  educationAnswers.familyIncome = e.target.value;
});
document.getElementById("coCreditScore")?.addEventListener("input", e => {
  educationAnswers.coCreditScore = e.target.value;
});

// ================= BUSINESS =================
const businessAnswers = {
  yearsOld: "",
  annualRevenue: "",
  monthlyExpenses: "",
  creditScore: "",
  existingEMIs: ""
};

document.getElementById("Q1")?.querySelector("input")?.addEventListener("input", e => {
  businessAnswers.yearsOld = e.target.value;
});
document.getElementById("Q2")?.querySelector("input")?.addEventListener("input", e => {
  businessAnswers.annualRevenue = e.target.value;
});
document.getElementById("Q3")?.querySelector("input")?.addEventListener("input", e => {
  businessAnswers.monthlyExpenses = e.target.value;
});
document.getElementById("Q4")?.querySelector("input")?.addEventListener("input", e => {
  businessAnswers.creditScore = e.target.value;
});
document.getElementById("Q5")?.querySelector("input")?.addEventListener("input", e => {
  businessAnswers.existingEMIs = e.target.value;
});

// ================= MEDICAL =================
const medicalAnswers = {
  treatmentCost: "",
  monthlyIncome: "",
  creditScore: "",
  healthInsurance: "",
  existingEMIs: ""
};

document.getElementById("Q1")?.querySelector("input")?.addEventListener("input", e => {
  medicalAnswers.treatmentCost = e.target.value;
});
document.getElementById("Q2")?.querySelector("input")?.addEventListener("input", e => {
  medicalAnswers.monthlyIncome = e.target.value;
});
document.getElementById("Q3")?.querySelector("input")?.addEventListener("input", e => {
  medicalAnswers.creditScore = e.target.value;
});
document.querySelectorAll("#Q4 .option-card").forEach(btn => {
  btn.addEventListener("click", () => {
    medicalAnswers.healthInsurance = btn.textContent;
  });
});
document.getElementById("Q5")?.querySelector("input")?.addEventListener("input", e => {
  medicalAnswers.existingEMIs = e.target.value;
});

// ================= PERSONAL =================
const personalAnswers = {
  employmentType: "",
  monthlyIncome: "",
  workExperience: "",
  totalEMIs: "",
  creditScore: "",
  age: ""
};

document.querySelectorAll("#Q1 .option-card").forEach(btn => {
  btn.addEventListener("click", () => {
    personalAnswers.employmentType = btn.textContent;
  });
});
document.getElementById("Q2")?.querySelector("input")?.addEventListener("input", e => {
  personalAnswers.monthlyIncome = e.target.value;
});
document.getElementById("Q3")?.querySelector("input")?.addEventListener("input", e => {
  personalAnswers.workExperience = e.target.value;
});
document.getElementById("Q4")?.querySelector("input")?.addEventListener("input", e => {
  personalAnswers.totalEMIs = e.target.value;
});
document.getElementById("Q5")?.querySelector("input")?.addEventListener("input", e => {
  personalAnswers.creditScore = e.target.value;
});
document.getElementById("Q6")?.querySelector("input")?.addEventListener("input", e => {
  personalAnswers.age = e.target.value;
});

// ================= PAYLOAD BUILDER =================
function buildPayload() {
  if (selectedLoanType === "Education") {
    return {
      loan_type: "Education",
      degree_level: educationAnswers.educationLevel,
      college_tier: educationAnswers.collegeTier,
      course_type: educationAnswers.courseNature,
      annual_fees: Number(educationAnswers.courseFee),
      family_income: Number(educationAnswers.familyIncome),
      co_applicant: educationAnswers.coApplicant,
      credit_score: Number(educationAnswers.coCreditScore)
    };
  }

  if (selectedLoanType === "Business") {
    return {
      loan_type: "Business",
      business_age: Number(businessAnswers.yearsOld),
      annual_revenue: Number(businessAnswers.annualRevenue),
      monthly_expenses: Number(businessAnswers.monthlyExpenses),
      credit_score: Number(businessAnswers.creditScore),
      existing_emis: Number(businessAnswers.existingEMIs)
    };
  }

  if (selectedLoanType === "Medical") {
    return {
      loan_type: "Medical",
      treatment_cost: Number(medicalAnswers.treatmentCost),
      monthly_income: Number(medicalAnswers.monthlyIncome),
      credit_score: Number(medicalAnswers.creditScore),
      insurance: medicalAnswers.healthInsurance,
      existing_emis: Number(medicalAnswers.existingEMIs)
    };
  }

  if (selectedLoanType === "Personal") {
    return {
      loan_type: "Personal",
      employment_type: personalAnswers.employmentType,
      monthly_income: Number(personalAnswers.monthlyIncome),
      job_experience: Number(personalAnswers.workExperience),
      existing_emis: Number(personalAnswers.totalEMIs),
      credit_score: Number(personalAnswers.creditScore),
      age: Number(personalAnswers.age)
    };
  }
  if (selectedLoanType === "Investment") {
  return {
    loan_type: "Investment",
    startup_stage: investmentAnswers.startupStage,
    industry: investmentAnswers.industry,
    monthly_revenue: Number(investmentAnswers.monthlyRevenue),
    growth_rate: Number(investmentAnswers.growthRate),
    founder_experience: investmentAnswers.founderExperience,
    funding_required: investmentAnswers.fundingRequired
  };
}

}

// ================= SUBMIT TO BACKEND =================
function submitToBackend() {
  const payload = buildPayload();

  console.log("SENDING TO BACKEND:", payload);

  localStorage.setItem("pendingPayload", JSON.stringify(payload));

  if (selectedLoanType === "Investment") {
    window.location.href = "loading_investment.html";
  } else {
    window.location.href = "loading.html";
  }
}


