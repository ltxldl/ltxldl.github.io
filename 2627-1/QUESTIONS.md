# Câu hỏi lớn cần giảng viên quyết — 2627-1

> Claude ghi vào đây khi gặp việc vượt thẩm quyền (thay đổi khung buổi, cơ chế chấm, nguồn dữ liệu đáng ngờ...) rồi chuyển sang việc khác, không dừng chờ. Mỗi mục có bối cảnh + phương án đề xuất.

## 2. Deck buổi 8: chỉ số mùa vụ "đỉnh T1–T4, đáy T9" là artefact của cửa sổ dữ liệu lệch — cần sửa nội dung?

**Phát hiện (06/07/2026, trong đợt 2 khi tính số liệu cho lab tuần 8):** hình `img/lecture-08/mua-vu.png` và slide "Nhịp mùa vụ — đo, đừng đoán" (+ slide giải thích "Vì sao đỉnh không nằm gọn ở hè T12–T2") dựa trên chỉ số tính từ cửa sổ **2022-01 → 2026-06**. Vì nửa đầu 2026 là nửa năm lớn nhất lịch sử và **chỉ góp mặt cho T1–T6**, các tháng đầu năm bị thổi phồng → "đỉnh T1–T4" (script: `gen_figures.py`, phần seasonality profile).

**Số kiểm chứng (visualisations/reviews.csv, snapshot 2026-06-29):**
- Cách của script (2022→06/2026): T3=121, T1=111, T4=110 (đỉnh) · T9=82 (đáy) — đúng như hình trong deck.
- Cửa sổ cân bằng (2022–2025 trọn năm): **T11=133, T8=125, T7=119, T10=118 (đỉnh) · T2=67 (đáy)**.
- Khử trend từng năm (chuẩn hoá mỗi năm rồi trung bình): y hệt — T11=133, T8=121 … đáy T2=68. Cả 4 năm 2022–2025, tháng 11 đều là tháng cao nhất năm (thấy ngay trong ma trận 4×12 của lab tuần 3).

**Hệ quả:** mùa vụ thật của review Santiago là **đỉnh đông–xuân (T7–T8, T10–T11), đáy hè (T2)** — hợp với một đô thị (mùa trượt tuyết + kỳ nghỉ đông Chile; dân địa phương rời thành phố vào hè) chứ không phải câu chuyện "review trễ sau kỳ nghỉ hè T12–T2 + T2 ngắn" như 2 slide hiện tại và ghi chú trong DECISIONS.md đợt 1. Câu chuyện "đo, đừng đoán" hoá ra tự nó đo bằng cửa sổ lệch — đúng loại bẫy "kỳ không trọn" mà chính buổi 8 dạy.

**Đề xuất (chờ thầy duyệt, Claude làm được ngay khi đồng ý):** sửa `gen_figures.py` (lọc 2022–2025 trọn năm), chạy lại hình; sửa 2 slide liên quan của deck 8 (tiêu đề "Đỉnh T1–T4…" → mùa vụ thật; slide giải thích đổi thành bài học kép: *đo mùa vụ phải dùng các năm trọn — và đô thị có mùa ngược điểm nghỉ dưỡng*); cập nhật cell tương ứng trong `notebooks/lecture-08.ipynb` + ghi chú đính chính vào DECISIONS.md. Slide "review trễ hơn chuyến đi" vẫn đúng như một hiện tượng (dịch đỉnh ~1 tháng) — chỉ sai khi dùng nó giải thích "đỉnh T1–T4".

**Trạng thái học liệu đợt 2:** lab tuần 3 và tuần 8 + giáo án TA đã viết theo hướng trung lập (chỉ nói "đếm thô trộn mùa vụ với đà tăng trưởng, muốn tách phải chuẩn hoá trong từng năm"), không lặp lại con số sai và không mâu thuẫn công khai với deck trong khi chờ quyết định.

## 1. BTL không còn thành phố châu Á nào — chấp nhận hay nới tiêu chí? ✅ ĐÃ QUYẾT

**Quyết định của giảng viên (06/07/2026):** giữ nguyên 12 thành phố chính; thêm **Bangkok / Singapore / Taipei làm thành phố đối chứng tuỳ chọn** (chỉ đối chứng — so sánh chéo trên snapshot mới nhất, không làm thành phố chính). Đã cập nhật ghi chú dưới bảng thành phố trong `projects/project_airbnb.html`.

**Bối cảnh (khảo sát 05/07/2026):** Inside Airbnb hiện chỉ còn giữ 2 snapshot trong 12 tháng gần nhất cho toàn bộ thành phố châu Á (Bangkok, Singapore, Taipei, Tokyo, Hong Kong: chỉ có bản 06/2026 + 09/2025) và cả nhiều thành phố lớn châu Âu (Paris, London, Berlin, Amsterdam, Rome). Tiêu chí trong yêu cầu đề ("≥3 snapshot trong ~12 tháng") loại hết các thành phố này. 12 thành phố được chọn vì vậy đều ở châu Âu (bán đảo Iberia) + châu Mỹ.

**Đã làm:** chọn 12 thành phố đạt chuẩn (xem DECISIONS.md), trong đề có giải thích và có nhóm nam bán cầu (Buenos Aires, Santiago, Rio) để khai thác tính mùa vụ ngược.

**Cần thầy quyết:** nếu muốn có 1–2 thành phố châu Á cho gần gũi sinh viên (Bangkok/Singapore/Taipei), phải chấp nhận nhóm đó chỉ có 2 snapshot (phân tích theo thời gian mỏng hơn) — khi đó nên giao kèm 1 thành phố đối chứng nhiều snapshot. Nếu thầy đồng ý, chỉ cần thêm dòng vào bảng thành phố trong `projects/project_airbnb.html`.
