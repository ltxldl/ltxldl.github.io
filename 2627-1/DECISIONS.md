# Quyết định nhỏ trong đợt dựng học liệu 2627-1

> Các quyết định Claude tự đưa ra theo hướng hợp lý (giảng viên có thể đảo lại). Câu hỏi lớn nằm ở QUESTIONS.md.

- **Highlight theme**: chuẩn hoá `zenburn.css` cho mọi deck (các deck mới nhất 2526-1 đều dùng zenburn; template cũ ghi monokai là sót).
- **Tên file deck**: `lecture-XX-<ten-khong-dau>.html`, ví dụ `lecture-11-llm-du-lieu-phi-cau-truc.html` (giữ convention gạch ngang của 2526-1, chuyển sang tiếng Việt không dấu).
- **Link notebook trong index**: trỏ thẳng Colab qua `colab.research.google.com/github/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/...` — chỉ hoạt động sau khi merge vào `main`; trong thời gian draft sẽ 404 (chấp nhận được).
- **Title slide**: giảng viên ghi "Nguyễn Tuấn Phong", trợ giảng để placeholder `{{cập nhật sau}}` (chưa có thông tin phân công 2627-1).
- **Hệ màu hộp nhấn** (theo style guide): cam `#E8890C` = điểm chốt, đỏ `#E62727` = cảnh báo/lỗi, xanh lá `#2E8B57` = khuyến nghị/ví dụ tốt, xanh lam `#1E93AB` = cấu trúc/định nghĩa/câu hỏi. Badge 🤖 "Làm với AI" dùng tím `#7A4CB0` để tách khỏi 4 màu nội dung.
- **Copy `package.json` + `gulpfile.js`** từ 2526-1 sang để giữ workflow `npm start` (speaker notes + livereload) cho ai cần.
- **VanderPlas 2nd ed**: link bản đọc online miễn phí `jakevdp.github.io/PythonDataScienceHandbook` (trang chính thức của sách; nội dung online là bản mở của sách).
- **BTL — 12 thành phố** (khảo sát thật 05/07/2026, tiêu chí ≥3 snapshot/12 tháng): Barcelona, Madrid, Lisbon, Porto, Montreal, Toronto, Vancouver, New York City, New Orleans, Buenos Aires, Santiago, Rio de Janeiro. Dự phòng: SF, Portland, Dallas, Boston, Quebec City, Brisbane, Budapest… Mỗi thành phố chốt 4 snapshot bắt buộc cách nhau ~1 quý (thành phố monthly được dùng thêm bản khác).
- **BTL — không commit dữ liệu thô** vào repo nhóm (file quá lớn, và cơ chế held-out yêu cầu script tải tự động theo config) — khác đề cũ 2526-1 vốn cho commit raw.
- **BTL — trọng số rubric**: A pipeline 30% / B dữ liệu (QA+KPI+LLM) 25% / C trực quan hoá & insight 25% / D nhóm & minh bạch AI 20%; thưởng tối đa +10%.
- **BTL — held-out**: chấm bằng snapshot phát hành trong kỳ (~09–12/2026) hoặc bản monthly không nằm trong danh sách bắt buộc; ghi rõ trong đề để nhóm thiết kế pipeline chịu được schema drift.
- **BTL — mốc nộp trung gian**: thêm mốc "bản đề xuất tuần 8" (QA/KPI/LLM dự kiến, GV phản hồi không chấm điểm) — để cứu các nhóm chọn sai hướng sớm.
- **Dữ liệu thật phát hiện khi soạn bài 8**: cột `host_since` trong snapshot Santiago 06/2026 trống 100% (Inside Airbnb thay bằng `hosts_time_as_*`); học liệu dùng `first_review` cho demo Timedelta. Mùa vụ review Santiago đỉnh T1–T4 (không phải T12–T2) — do review trễ hơn chuyến đi + T2 ngắn; đưa thẳng vào bài giảng làm ví dụ "đo, đừng đoán".
- **Buổi 14 — phát hiện khi kiểm chứng số liệu**: bảng `reviews` của một snapshot bị right-censoring ở đuôi (T9/2025 "mọc thêm" 21% khi nhìn từ snapshot 06/2026) và lịch sử co giãn vì listing rời sàn mang theo review (T8/2025 giảm 18% giữa 2 snapshot). Kịch bản audit KL3 đổi từ "sai mùa vụ" thành "không kiểm được từ 1 snapshot" — trung thực với dữ liệu và dạy thêm được loại phán quyết thứ ba.
- **Rà soát render (Playwright, khung 960×700)**: đo scrollHeight/Width từng slide của cả 15 deck — 103 slide tràn do font gốc 40px của theme trắng quá lớn với tiếng Việt. Chỉnh hệ thiết kế trong `lecture-style.css` (font gốc 36px, hộp nhấn/pipeline/bảng gọn hơn) thay vì sửa lẻ từng slide; 6 slide còn lại sửa nội dung (tách checklist buổi 15 thành 2 slide, gọt chữ). Kết quả cuối: **0 slide tràn**, không ảnh hỏng, không lỗi JS.
