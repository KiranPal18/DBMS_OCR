import os

# Define the LaTeX content for the test brochure
latex_content = r"""
\documentclass[a4paper,11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{enumitem}

\definecolor{primary}{RGB}{0, 51, 102}
\titleformat{\section}{\large\bfseries\color{primary}}{}{0em}{}[\titlerule]

\begin{document}

\begin{center}
    {\Huge \textbf{\color{primary} TechNova Solutions}} \\
    \vspace{2mm}
    {\large \textit{Innovating the Future of Fintech}} \\
    \vspace{4mm}
    \textbf{Internship Opportunity - Summer 2026}
\end{center}

\vspace{10mm}

\section{Company Overview}
TechNova Solutions is a leading global technology firm specializing in High-Frequency Trading (HFT) and AI-driven financial analytics. With an annual turnover exceeding \$500 Million, we operate at the intersection of mathematics and high-performance computing.

\vspace{5mm}

\section{Job Description}
\textbf{Role:} Machine Learning Intern \\
\textbf{Type:} 2-Month Summer Internship \\
\textbf{Location:} Bangalore (On-site)

\vspace{5mm}

\section{Eligibility Criteria}
\begin{itemize}[noitemsep]
    \item Open to 2nd and 3rd-year B.Tech students.
    \item Eligible Branches: CSE, MnC, EE, and ECE.
    \item Minimum CGPA: 8.0 and above.
\end{itemize}

\vspace{5mm}

\section{Compensation \& Benefits}
\begin{itemize}[noitemsep]
    \item \textbf{Stipend:} INR 60,000 per month.
    \item \textbf{PPO Compensation:} Up to 24 LPA (Base + Performance Bonus).
    \item Perks: Subsidized meals, travel allowance, and health insurance.
\end{itemize}

\vspace{5mm}

\section{Selection Process}
The recruitment drive will consist of the following stages:
\begin{enumerate}[noitemsep]
    \item Resume Shortlisting based on academic performance.
    \item Online Technical Assessment (Data Structures, Algorithms, and ML Basics).
    \item Deep Technical Interview focused on Mathematics and Coding.
    \item Cultural Fit \& HR Round.
\end{enumerate}

\vspace{5mm}

\section{Important Dates \& Contact}
\textbf{Application Deadline:} May 15, 2026 \\
\textbf{Headquarters:} 12th Floor, Cyber Plaza, Whitefield, Bangalore - 560066 \\
\textbf{Website:} www.technovasolutions.ai

\end{document}
"""

# Save to .tex and compile
with open("technova_brochure.tex", "w") as f:
    f.write(latex_content)

import subprocess
subprocess.run(["pdflatex", "-interaction=nonstopmode", "technova_brochure.tex"])