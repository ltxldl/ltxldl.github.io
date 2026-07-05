# Nhiệm vụ: Dựng toàn bộ học liệu học kỳ 2627-1 — Lập trình xử lý dữ liệu

Bạn đang ở repo học liệu môn Lập trình xử lý dữ liệu (UET.DSE2049). Đây là một session dài chạy tự chủ, không có giảng viên giám sát realtime. Nhiệm vụ: dựng hoàn chỉnh học liệu học kỳ 1 năm học 2026–2027 trong thư mục `2627-1/`.

## Bước 0 — đọc trước khi làm bất cứ điều gì

1. `CLAUDE.md` — quy ước repo, các quyết định đã chốt, **khung 15 buổi** (nguồn chân lý về nội dung từng buổi).
2. `SLIDE_STYLE_GUIDE.md` — tiêu chuẩn slide, đọc kỹ cả ghi chú chuyển thể ở đầu file. Mọi deck phải đạt rubric A–E của guide này.
3. Xem 2–3 deck trong `2526-1/` (ví dụ `lecture-06-pandas.html`, `lecture-09-visualization.html`) để nắm hạ tầng Reveal.js, và `2526-1/projects/project_4.html` để nắm format một trang đề bài tập lớn.

## Sản phẩm cần bàn giao

Tất cả bằng **tiếng Việt** (quy ước thuật ngữ Anh–Việt theo ghi chú đầu SLIDE_STYLE_GUIDE.md):

1. **15 deck slide** theo đúng khung 15 buổi trong CLAUDE.md. Buổi 9 chỉ là deck ôn tập giữa kỳ ngắn; buổi 15 là deck hướng dẫn vấn đáp + checklist nộp BTL. Mỗi deck nội dung (1–8, 10–14) kết bằng mục "Làm với AI thì sao?" (2–3 slide).
2. **13 notebook Colab** (`notebooks/lecture-XX.ipynb`, các buổi 1–8 và 10–14): mục tiêu buổi học → demo bám slide → bài tập tại lớp (ô TODO) → 1 bài thử thách. Chạy được từ đầu đến cuối trên Colab; dữ liệu demo nhỏ tải qua URL hoặc sinh ngay trong notebook.
3. **01 đề bài tập lớn Inside Airbnb** (`projects/project_airbnb.html` + `projects/index.html`) — yêu cầu chi tiết ở mục riêng bên dưới.
4. **Trang chính sách AI** của môn (trang riêng `ai-policy.html`, link từ index và nhắc trong deck buổi 1): công cụ được phép; nghĩa vụ khai báo; hai chế độ đánh giá đóng/mở; ranh giới gian lận (dùng AI trong quiz/giữa kỳ, giấu việc dùng AI); hậu quả.
5. **`index.html` của học kỳ** (bảng lịch 15 buổi: link slide + notebook + đồ án) và cập nhật `index.html` root (thêm thẻ học kỳ mới, chuyển nhãn "Hiện hành").
6. **`lecture-template.html` mới** chuẩn hoá theo style guide (làm trước khi viết 15 deck; các pattern lặp — badge 📖 Tự học, hộp nhấn, caption, layout hai cột, khối code+output — đưa vào `lecture-style.css`, không inline lặp).

**Không làm đợt này:** bài tập về nhà hàng tuần, đề thi giữa kỳ (giảng viên làm sau).

## Đề bài tập lớn Inside Airbnb — yêu cầu nội dung

Format tham khảo `2526-1/projects/project_4.html` (đề Airbnb cũ), nhưng viết lại theo các nguyên tắc:

- Giữ khung: thu thập → làm sạch/QA → tổng hợp KPI → trực quan hoá → báo cáo; nhóm; GitHub repo private mời giảng viên; vấn đáp.
- **Phân công**: mỗi nhóm 1 thành phố chính + 1–2 thành phố đối chứng. Chọn ~10–12 thành phố trên insideairbnb.com có ≥3 snapshot trong ~12 tháng gần nhất, liệt kê cụ thể tên + ngày snapshot trong đề. Danh sách nhóm/link spreadsheet để placeholder `{{...}}`.
- **Bớt cầm tay chỉ việc**: nêu yêu cầu sản phẩm và tiêu chuẩn chất lượng, nhưng nhóm phải TỰ đề xuất bộ quy tắc QA và bộ KPI (có công thức/đơn vị) rồi bảo vệ lựa chọn khi vấn đáp — ghi rõ điều này trong đề.
- **Hợp phần LLM bắt buộc** trên bảng `reviews`: dùng Gemini API (free tier) trích xuất thông tin có cấu trúc (ví dụ khía cạnh được khen/chê, cảm xúc, ngôn ngữ) → so sánh với một baseline không-LLM → tự gán nhãn tay ≥100 mẫu làm bộ đánh giá → báo cáo chất lượng (accuracy/agreement) + chi phí/quota. 
- **Minh bạch AI**: bắt buộc file `AI_USAGE.md` trong repo nhóm (công cụ đã dùng, các prompt then chốt, AI sai ở đâu, đã kiểm chứng thế nào).
- **Tái lập được**: pipeline chạy end-to-end bằng MỘT lệnh từ dữ liệu thô đến hình/bảng cuối. Ghi rõ trong đề: khi chấm, giảng viên sẽ chạy pipeline trên **một snapshot giữ lại** không nằm trong danh sách nhóm đã xử lý — pipeline phải chạy được và kết quả phải nhất quán.
- **Rubric chấm** trong đề: bám 4 nhóm tiêu chí của đề cương (thiết kế pipeline / lưu trữ & thao tác dữ liệu / trực quan hoá & insight / làm việc nhóm & đạo đức-minh bạch AI), mỗi tiêu chí có mô tả 4 mức; ghi rõ vấn đáp hỏi riêng từng thành viên (giải thích đoạn code bất kỳ + live task nhỏ) và điểm thành viên được phép lệch nhau.
- Deadline các mốc: để placeholder `{{...}}`.

## Quy trình làm việc

- **Branch**: làm toàn bộ trên branch `2627-1-draft`. TUYỆT ĐỐI không push lên `main` — main auto-deploy GitHub Pages công khai. Commit sau mỗi deliverable hoàn chỉnh, message tiếng Việt ngắn gọn.
- **Thứ tự làm** (để giảng viên review được sớm những phần rủi ro nhất):
  1. Skeleton `2627-1/` (copy hạ tầng reveal.js từ `2526-1/`, dọn nội dung cũ) + template mới + CSS pattern + index nháp.
  2. Trang chính sách AI.
  3. Đề BTL Airbnb (kiểm tra thực tế trên insideairbnb.com/get-the-data: thành phố nào đủ snapshot, cột nào có trong `reviews` — đừng bịa schema).
  4. Buổi 11 (deck + notebook) — nội dung mới nhất, cần ý kiến giảng viên sớm nhất.
  5. Các buổi còn lại tuần tự 1 → 14 (xong deck + notebook buổi nào verify buổi đó), cuối cùng buổi 9 và 15.
  6. Rà soát toàn cục: chạy rubric A–E của style guide trên từng deck, chạy lại toàn bộ notebook, kiểm tra link trong index.
- **Verify từng deck**: serve từ ROOT repo (xem CLAUDE.md), mở từng deck kiểm tra render — ảnh hiển thị, không tràn/cắt nội dung ở khung 960×700 mặc định của Reveal, code highlight đúng.
- **Notebook + API key**: code Gemini đọc key từ `userdata` (Colab) hoặc biến môi trường `GEMINI_API_KEY`; luôn có đường "chạy không key" bằng output đã cache để notebook vẫn chạy end-to-end khi không có key.
- **Quyết định nhỏ** (chọn dataset demo, đặt tên file, cắt/giữ một mục con...): tự quyết theo hướng hợp lý, ghi một dòng vào `2627-1/DECISIONS.md`. **Câu hỏi lớn** (thay đổi khung buổi, thay đổi cơ chế chấm, nghi ngờ nguồn dữ liệu không dùng được...): ghi vào `2627-1/QUESTIONS.md` rồi chuyển sang việc khác — không dừng chờ, không tự ý quyết.
- **Tiến độ**: duy trì `2627-1/PROGRESS.md` — checklist toàn bộ deliverables, cập nhật ngay sau mỗi mục hoàn thành. Đây là nơi giảng viên nhìn vào đầu tiên khi quay lại.
- **Dữ liệu**: không commit dữ liệu Airbnb thật vào repo (chỉ script tải + file demo nhỏ cho notebook); không đưa bất kỳ thông tin sinh viên nào vào repo.

## Tiêu chí hoàn thành

- [ ] 15 deck đạt rubric style guide, tiếng Việt tự nhiên, 30–40 slide thực dạy/deck nội dung, có mục "Làm với AI thì sao?" (trừ buổi 9, 15)
- [ ] 13 notebook chạy end-to-end trên Colab (buổi 11 chạy được cả khi không có API key nhờ output cache)
- [ ] Đề BTL Airbnb đầy đủ: danh sách thành phố + snapshot thật, hợp phần LLM, `AI_USAGE.md`, cơ chế chấm held-out, rubric 4 tiêu chí, placeholder cho deadline/phân công
- [ ] Chính sách AI + index học kỳ + index root cập nhật
- [ ] `PROGRESS.md` / `DECISIONS.md` / `QUESTIONS.md` phản ánh đúng trạng thái cuối
