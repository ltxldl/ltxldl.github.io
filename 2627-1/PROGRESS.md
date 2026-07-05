# Tiến độ dựng học liệu 2627-1

> File này do Claude duy trì trong đợt dựng học liệu (07/2026). Giảng viên xem ở đây trước tiên.
> Trạng thái: ⬜ chưa làm · 🟨 đang làm · ✅ xong (đã verify) · ⏸️ chờ ý kiến (xem QUESTIONS.md)

## 1. Hạ tầng & khung

- ✅ Skeleton `2627-1/` (revealjs + plugin copy từ 2526-1, thư mục img/ notebooks/ projects/)
- ✅ `lecture-style.css` — bổ sung pattern: badge 📖 Tự học + 🤖 AI, hộp nhấn (key/warn/good), hai cột, figure+caption, compact-table, jp-cell
- ✅ `lecture-template.html` mới theo SLIDE_STYLE_GUIDE.md (tiếng Việt, minh hoạ đủ pattern)
- ✅ `index.html` học kỳ (bảng 15 buổi, link slide + notebook Colab + BTL + chính sách AI)
- ✅ `index.html` root (thêm thẻ 2627-1 "Hiện hành", 2526-1 → "Đã kết thúc")

## 2. Chính sách AI

- ⬜ `ai-policy.html` — trang chính sách AI của môn

## 3. Bài tập lớn Inside Airbnb

- ⬜ Khảo sát insideairbnb.com/get-the-data (thành phố + snapshot thật, schema `reviews`)
- ⬜ `projects/project_airbnb.html`
- ⬜ `projects/index.html`

## 4. Slide + notebook từng buổi

| Buổi | Deck | Notebook |
|---|---|---|
| 1. Tổng quan & chính sách AI | ⬜ | ⬜ |
| 2. Python cơ bản | ⬜ | ⬜ |
| 3. NumPy | ⬜ | ⬜ |
| 4. Làm quen pandas | ⬜ | ⬜ |
| 5. Series & DataFrame chuyên sâu | ⬜ | ⬜ |
| 6. Kết nối & truy xuất dữ liệu ngoài | ⬜ | ⬜ |
| 7. Xử lý dữ liệu chuỗi | ⬜ | ⬜ |
| 8. Xử lý dữ liệu thời gian | ⬜ | ⬜ |
| 9. Ôn tập giữa kỳ (deck ngắn) | ⬜ | — |
| 10. Làm sạch dữ liệu có cấu trúc | ⬜ | ⬜ |
| 11. LLM & dữ liệu phi cấu trúc | ⬜ | ⬜ |
| 12. Trực quan hoá cơ bản | ⬜ | ⬜ |
| 13. Trực quan hoá nâng cao | ⬜ | ⬜ |
| 14. Kể chuyện bằng dữ liệu | ⬜ | ⬜ |
| 15. Hướng dẫn vấn đáp BTL (deck) | ⬜ | — |

## 5. Rà soát toàn cục

- ⬜ Rubric A–E của style guide trên từng deck
- ⬜ Chạy lại toàn bộ notebook end-to-end
- ⬜ Kiểm tra render từng deck (khung 960×700, ảnh, tràn nội dung)
- ⬜ Kiểm tra toàn bộ link trong index

## Việc giảng viên cần làm (ngoài phạm vi đợt này)

- Điền placeholder `{{...}}`: trợ giảng, link spreadsheet phân công nhóm, deadline các mốc BTL
- Bài tập về nhà hàng tuần + đề thi giữa kỳ (đợt sau)
- Duyệt nội dung rồi merge `2627-1-draft` → `main`
