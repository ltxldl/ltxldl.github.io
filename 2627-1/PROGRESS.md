# Tiến độ học liệu 2627-1

> File này do Claude duy trì. Đợt 1 (dựng 15 deck + 13 notebook demo + đề BTL) đã xong 05/07/2026 — chi tiết giữ nguyên bên dưới. Đợt 2 (edit-pass văn phong + học liệu giờ thực hành, theo `STARTER-PROMPT-2627-1-DOT2.md`) bắt đầu 07/2026 — trạng thái ở mục ngay dưới đây.

## Đợt 2 — sửa văn phong + học liệu giờ thực hành (đang làm)

| Deliverable | Trạng thái |
|---|---|
| **Bộ mẫu tuần 2** (lab-02.ipynb + ta-guide-02 + micro-02) | ✅ 06/07 — chờ giảng viên duyệt; lab đã chạy end-to-end (bản điền đáp án, mọi assert qua trên snapshot thật) |
| Việc A: `.pipeline` sửa gốc CSS + bỏ inline | ✅ 06/07 — font-size 0.7em ở rule gốc, bỏ 2 inline buổi 1 |
| Việc A: edit-pass văn phong deck 2–15 + đo tràn | ✅ 06/07 — 14 deck + template; đo từng deck sau sửa: **0 slide tràn trên cả 15 deck**; sửa thêm 2 tràn có sẵn (buổi 9, 13) + đồng bộ "trình bày 5'" ở buổi 15 (chi tiết: DECISIONS.md) |
| Việc A: pass nhẹ markdown 13 notebook demo | ✅ 06/07 — 36 cell: BTL→bài tập lớn, nghi thức→thói quen, hôm nay→buổi này, bỏ 😉, nghĩa vụ→trách nhiệm |
| Việc B: lab + TA guide + micro các tuần còn lại | ⬜ (1/13 lab, 1/15 guide, 1/13 micro) |
| Index học kỳ: link lab từng buổi | ⬜ |
| Rà soát cuối (lab end-to-end, tràn 15 deck, private/ sạch) | ⬜ |

**Lấy thư mục private/ (KHÔNG có trên git):** học liệu trợ giảng nằm ở `2627-1/private/` trên máy làm việc này — xem `2627-1/private/README.md` (có sẵn lệnh `scp`/`tar` và quy trình phát cho TA qua Canvas Portal).

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
- ✅ QUESTIONS.md #1 đã quyết (06/07/2026): giữ 12 thành phố chính; Bangkok/Singapore/Taipei thêm làm đối chứng tuỳ chọn

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

## Giảng viên cần làm (cập nhật 06/07/2026 — sau khi đã điền các quyết định)

> Các placeholder đã được xử lý ngày 06/07/2026 theo quyết định của giảng viên (xem cuối DECISIONS.md): bỏ thông tin GV/TA, kênh lớp = Canvas, nhóm 4–5 SV, mốc deadline theo tuần học, vấn đáp ~20'/nhóm, giữa kỳ viết giấy. Placeholder duy nhất còn lại: thời lượng & cấu trúc điểm giữa kỳ (deck buổi 9).

1. **Công bố trên Canvas đầu kỳ**: spreadsheet phân công nhóm/thành phố, danh sách tài khoản GitHub của GV/TA (để nhóm mời vào repo), ngày cụ thể cho các mốc tuần 3/8/14/15 (khi có thời khoá biểu), lịch vấn đáp buổi 15.
2. **Điền thời lượng & cấu trúc điểm giữa kỳ** vào deck buổi 9 (`{{cập nhật trước ngày thi}}`) — trước ngày thi.
3. Soạn **bài tập về nhà hàng tuần + đề thi giữa kỳ** (đợt sau, theo kế hoạch). Riêng **học liệu giờ thực hành + edit-pass văn phong**: đã lên kế hoạch đợt 2 (07/07/2026) — xem `STARTER-PROMPT-2627-1-DOT2.md` ở root và `2627-1/EDIT-PASS-NOTES.md`
4. Duyệt nội dung → merge `2627-1-draft` vào `main` để public + kích hoạt link Colab
5. (Khuyến nghị) Trước học kỳ: xem lại quota free tier Gemini trong AI Studio và chạy notebook buổi 11 một lần với API key thật
