import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Consult a Doctor",
    page_icon="👨‍⚕️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- STYLES ----------------
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.block-container {
    max-width: 900px;
    padding-top: 50px;
}

/* Header */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 600;
    color: #00f5ff;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    color: #d0d0d0;
    opacity: 0.85;
    margin-bottom: 40px;
}

/* Doctor Card */
.card {
    background: #1c1c1c;
    border-radius: 18px;
    padding: 18px;
    display: flex;
    gap: 18px;
    align-items: center;
    margin-bottom: 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.45);
    transition: 0.25s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 35px rgba(0,245,255,0.25);
}

/* Image */
.card img {
    width: 160px;
    height: 160px;
    object-fit: cover;
    border-radius: 14px;
    flex-shrink: 0;
}

/* Content */
.card-content {
    flex: 1;
}

.name {
    color: #00f5ff;
    font-size: 18px;
    font-weight: 600;
}

.spec {
    color: #cfcfcf;
    font-size: 14px;
    margin-top: 4px;
}

.exp {
    color: #9aa;
    font-size: 13px;
    margin: 6px 0 14px;
}

.book-btn {
    background-color: #00f5ff;
    color: black;
    font-weight: 600;
    padding: 10px 16px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: 0.2s;
}

.book-btn:hover {
    background-color: #00cdd4;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>Consult a Doctor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Choose from 20 experienced medical specialists</div>", unsafe_allow_html=True)

# ---------------- DOCTOR DATA (20 DOCTORS) ----------------
doctors = [
    ("Dr. Aarav Mehta", "Cardiologist", "10+ Years", "https://images.unsplash.com/photo-1622253692010-333f2da6031d"),
    ("Dr. Ananya Singh", "Dermatologist", "8+ Years", "https://images.unsplash.com/photo-1550831107-1553da8c8464"),
    ("Dr. Rohan Verma", "Neurologist", "12+ Years", "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d"),
    ("Dr. Priya Sharma", "Gynecologist", "9+ Years", "https://images.unsplash.com/photo-1607746882042-944635dfe10e"),
    ("Dr. Kabir Malhotra", "Orthopedic", "11+ Years", "https://images.unsplash.com/photo-1629909613654-28e377c37b09"),
    ("Dr. Sneha Iyer", "ENT Specialist", "7+ Years", "https://images.unsplash.com/photo-1594824476967-48c8b964273f"),
    ("Dr. Arjun Patel", "General Physician", "15+ Years", "https://images.unsplash.com/photo-1618498082410-b4aa22193b38"),
    ("Dr. Neha Kapoor", "Psychiatrist", "6+ Years", "https://images.unsplash.com/photo-1559839734-2b71ea197ec2"),
    ("Dr. Rahul Khanna", "Pulmonologist", "13+ Years", "https://images.unsplash.com/photo-1582750433449-648ed127bb54"),
    ("Dr. Pooja Nair", "Endocrinologist", "9+ Years", "https://images.unsplash.com/photo-1623854767648-e7bb8009f0db"),
    ("Dr. Sandeep Joshi", "Urologist", "14+ Years", "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d"),
    ("Dr. Ritu Bansal", "Oncologist", "10+ Years", "https://images.unsplash.com/photo-1551601651-2a8555f1a136"),
    ("Dr. Aman Choudhary", "Nephrologist", "8+ Years", "https://images.unsplash.com/photo-1612531386530-97286d97c2d2"),
    ("Dr. Shalini Gupta", "Pediatrician", "11+ Years", "https://images.unsplash.com/photo-1559839734-2b71ea197ec2"),
    ("Dr. Mohit Saxena", "Gastroenterologist", "12+ Years", "https://images.unsplash.com/photo-1537368910025-700350fe46c7"),
    ("Dr. Tanya Roy", "Rheumatologist", "7+ Years", "https://images.unsplash.com/photo-1598257006458-087169a1f08d"),
    ("Dr. Nikhil Jain", "Surgeon", "16+ Years", "https://images.unsplash.com/photo-1582750433449-648ed127bb54"),
    ("Dr. Kavita Menon", "Dietician", "6+ Years", "https://images.unsplash.com/photo-1606811971618-4486d14f3f99"),
    ("Dr. Rajeev Arora", "Radiologist", "14+ Years", "https://images.unsplash.com/photo-1618498082410-b4aa22193b38"),
    ("Dr. Meera Kulkarni", "Ophthalmologist", "9+ Years", "https://images.unsplash.com/photo-1594824476967-48c8b964273f"),
]

# ---------------- DISPLAY DOCTORS ----------------
for doc in doctors:
    st.markdown(f"""
    <div class="card">
        <img src="{doc[3]}" />
        <div class="card-content">
            <div class="name">{doc[0]}</div>
            <div class="spec">{doc[1]}</div>
            <div class="exp">{doc[2]}</div>
            <button class="book-btn">📅 Book Consultation</button>
        </div>
    </div>
    """, unsafe_allow_html=True)





