# Tiến độ dựng học liệu 2627-1 — HOÀN THÀNH ĐỢT DỰNG (05/07/2026)

> File này do Claude duy trì trong đợt dựng học liệu (07/2026). Toàn bộ deliverables của đợt đã xong và đã qua rà soát tự động; các mục "giảng viên cần làm" ở cuối file.

## 1. Hạ tầng & khung — ✅

- ✅ Skeleton `2627-1/` (revealjs 5.2.1 + plugin copy từ 2526-1; img/ notebooks/ projects/)
- ✅ `lecture-style.css` — pattern chuẩn hoá: badge 📖/🤖, hộp nhấn key/warn/good, two-col, figure+caption, compact-table, pipeline, jp-cell; hệ mật độ đã tinh chỉnh sau rà soát render (font gốc 36px)
- ✅ `lecture-template.html` mới theo SLIDE_STYLE_GUIDE.md (minh hoạ đủ pattern)
- ✅ `index.html` học kỳ (lịch 15 buổi + link Colab + BTL + chính sách AI) · `index.html` root đã thêm thẻ 2627-1 "Hiện hành"

## 2. Chính sách AI — ✅

- ✅ `ai-policy.html`: hai chế độ 🔒/🔓, công cụ được phép, 3 nghĩa vụ, ranh giới gian lận, hậu quả

## 3. Bài tập lớn Inside Airbnb — ✅

- ✅ Khảo sát thật insideairbnb.com (05/07/2026): 12 thành phố đạt chuẩn ≥3 snapshot/12 tháng (Barcelona, Madrid, Lisbon, Porto, Montreal, Toronto, Vancouver, NYC, New Orleans, Buenos Aires, Santiago, Rio), ngày snapshot + dataRoot ghi trong đề; schema `reviews`/`listings`/`calendar` xác minh (phát hiện: schema drift 79→90 cột, `calendar` mất cột giá, `host_since` trống 100% ở bản 06/2026, giá chuỗi theo nội tệ)
- ✅ `projects/project_airbnb.html`: nhóm tự đề xuất QA/KPI và bảo vệ; hợp phần LLM bắt buộc (Gemini structured output + baseline + ≥100 nhãn tay + chi phí + `--skip-llm`); `AI_USAGE.md`; chấm held-out snapshot; vấn đáp cá nhân; rubric 4 tiêu chí × 4 mức (30/25/25/20); placeholder deadline/phân công
- ✅ `projects/index.html`
- ⏸️ Xem QUESTIONS.md #1: không còn thành phố châu Á nào đủ chuẩn snapshot — cần thầy quyết có nới tiêu chí không

## 4. Slide + notebook từng buổi — ✅ 15/15 deck, 13/13 notebook

| Buổi | Deck | Notebook | Ghi chú |
|---|---|---|---|
| 1. Tổng quan & chính sách AI | ✅ 34 slide | ✅ | quy trình 5 bước làm việc với AI |
| 2. Python cơ bản | ✅ 34 | ✅ | lăng kính dữ liệu; `clean_price` ra đời |
| 3. NumPy | ✅ 36 | ✅ | 3 hình sinh script (speed/broadcast/axis) |
| 4. Làm quen pandas | ✅ 35 | ✅ | dữ liệu Santiago thật xuyên suốt từ đây |
| 5. Series & DataFrame chuyên sâu | ✅ 32 | ✅ | 2 hình (split-apply-combine, merge-how) |
| 6. Kết nối & truy xuất dữ liệu | ✅ 31 | ✅ | Parquet đo thật, API Open-Meteo, DuckDB |
| 7. Chuỗi & regex | ✅ 28 | ✅ | amenities/explode; baseline cho buổi 11 |
| 8. Dữ liệu thời gian | ✅ 26 | ✅ | mùa vụ + COVID từ 690k review thật |
| 9. Ôn tập giữa kỳ | ✅ 16 | — | 21 câu tự kiểm + 2 câu mẫu |
| 10. Làm sạch dữ liệu | ✅ 33 | ✅ | bộ quy tắc QA + qa_report chuẩn BTL |
| 11. LLM & phi cấu trúc | ✅ 40 | ✅ | Interactions API 2026 xác minh từ SDK; chạy trọn không cần key nhờ cache |
| 12. Trực quan hoá cơ bản | ✅ 27 | ✅ | 7 hình sinh script từ dữ liệu thật |
| 13. Trực quan hoá nâng cao | ✅ 30 | ✅ | choropleth geojson thật + 3 "hình AI lỗi" |
| 14. Kể chuyện & audit AI | ✅ 25 | ✅ | audit 5 kết luận AI, số liệu thật 100% |
| 15. Vấn đáp BTL | ✅ 16 | — | checklist nộp + kịch bản vấn đáp |

Mỗi deck nội dung kết bằng mục "Làm với AI thì sao?" (đã kiểm tự động). Mọi hình đều có script tái sinh trong `img/lecture-XX/scripts/`.

## 5. Rà soát toàn cục — ✅

- ✅ **Render 960×700** (Playwright/Chromium, đo scrollHeight/Width từng slide của cả 15 deck): **0 slide tràn**, 0 ảnh hỏng, 0 lỗi JS. (Ban đầu 103 slide tràn — nguyên nhân hệ thống là font gốc 40px; đã chỉnh hệ mật độ trong CSS + sửa nội dung 6 slide.)
- ✅ **13/13 notebook** chạy sạch end-to-end lần chốt trong môi trường mới (pandas 3.0.3; buổi 11 chạy trọn không cần API key nhờ cache)
- ✅ **Link nội bộ**: toàn bộ href/src trong index/deck/projects đều tồn tại (link Colab dạng `blob/main/...` sẽ hoạt động sau khi merge vào `main`)
- ✅ **Cấu trúc bắt buộc từng deck** (kiểm tự động): footer, title slide GV, agenda "Hôm nay", "Tổng kết", mục AI + badge, zenburn, `lang="vi"` — đủ 100%
- ✅ Rubric A–E áp khi viết từng deck; mọi output code trong slide đối chiếu với kết quả chạy thật (nhiều số nháp đã bị thay bằng số thật trong quá trình kiểm)

## Giảng viên cần làm (ngoài phạm vi đợt này)

1. **Điền placeholder `{{...}}`** — vị trí đầy đủ:
   - Mọi deck: `{{cập nhật sau}}` = tên trợ giảng ở title slide
   - `index.html`, `projects/index.html`, `project_airbnb.html`: link spreadsheet phân công nhóm
   - `project_airbnb.html`: 4 mốc deadline (tuần 3/8/14/15), cỡ nhóm, tài khoản GitHub trợ giảng
   - Buổi 1: kênh liên lạc + cỡ nhóm · Buổi 9: thời lượng/cấu trúc điểm thi · Buổi 14: hạn nộp · Buổi 15: hạn nộp + lịch vấn đáp + thời lượng phiên
2. **Trả lời QUESTIONS.md** (1 câu: thành phố châu Á cho BTL)
3. Soạn **bài tập về nhà hàng tuần + đề thi giữa kỳ** (đợt sau, theo kế hoạch)
4. Duyệt nội dung → merge `2627-1-draft` vào `main` để public + kích hoạt link Colab
5. (Khuyến nghị) Trước học kỳ: xem lại quota free tier Gemini trong AI Studio và chạy notebook buổi 11 một lần với API key thật
