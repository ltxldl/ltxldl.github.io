# Quyết định nhỏ trong đợt dựng học liệu 2627-1

> Các quyết định Claude tự đưa ra theo hướng hợp lý (giảng viên có thể đảo lại). Câu hỏi lớn nằm ở QUESTIONS.md.

- **Highlight theme**: chuẩn hoá `zenburn.css` cho mọi deck (các deck mới nhất 2526-1 đều dùng zenburn; template cũ ghi monokai là sót).
- **Tên file deck**: `lecture-XX-<ten-khong-dau>.html`, ví dụ `lecture-11-llm-du-lieu-phi-cau-truc.html` (giữ convention gạch ngang của 2526-1, chuyển sang tiếng Việt không dấu).
- **Link notebook trong index**: trỏ thẳng Colab qua `colab.research.google.com/github/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/...` — chỉ hoạt động sau khi merge vào `main`; trong thời gian draft sẽ 404 (chấp nhận được).
- **Title slide**: giảng viên ghi "Nguyễn Tuấn Phong", trợ giảng để placeholder `{{cập nhật sau}}` (chưa có thông tin phân công 2627-1).
- **Hệ màu hộp nhấn** (theo style guide): cam `#E8890C` = điểm chốt, đỏ `#E62727` = cảnh báo/lỗi, xanh lá `#2E8B57` = khuyến nghị/ví dụ tốt, xanh lam `#1E93AB` = cấu trúc/định nghĩa/câu hỏi. Badge 🤖 "Làm với AI" dùng tím `#7A4CB0` để tách khỏi 4 màu nội dung.
- **Copy `package.json` + `gulpfile.js`** từ 2526-1 sang để giữ workflow `npm start` (speaker notes + livereload) cho ai cần.
- **VanderPlas 2nd ed**: link bản đọc online miễn phí `jakevdp.github.io/PythonDataScienceHandbook` (trang chính thức của sách; nội dung online là bản mở của sách).
