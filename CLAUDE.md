# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Tổng quan

Repo học liệu môn **Lập trình xử lý dữ liệu** (UET.DSE2049), Viện Trí tuệ nhân tạo, Trường ĐH Công nghệ, ĐHQGHN. Giảng viên phụ trách: TS. Nguyễn Tuấn Phong. Giao tiếp với giảng viên bằng **tiếng Việt**.

Nội dung là website tĩnh (không có bước build/test/lint cho học liệu): trang index + slide bài giảng Reveal.js + trang mô tả bài tập lớn. Deploy qua GitHub Pages từ nhánh `main` — **mọi thứ push lên `main` là public ngay lập tức**.

File `UET_Đề cương học phần_*.docx` ở root là đề cương chính thức (bản 06/2025) — nguồn chân lý về khung 15 buổi, CLO và trọng số đánh giá (20% quiz / 20% giữa kỳ / 60% bài tập lớn nhóm). Thay đổi CLO, khung rubric hoặc trọng số phải qua phê duyệt Viện/Trường; nội dung bài giảng, đề bài tập và cách tổ chức chấm thì giảng viên tự quyết được.

## Cấu trúc

- Mỗi học kỳ một thư mục: `2526-1/` = HK1 2025–2026 (đã dạy xong, coi như **archive — không sửa nội dung giảng dạy trong đó**, chỉ dùng làm nguồn copy). `2627-1/` = kỳ tới, đã dựng xong trên nhánh `2627-1-draft`, đang được giảng viên duyệt dần và public theo từng đợt (xem mục Quy trình publish).
- `index.html` (root) — trang tổng liệt kê các học kỳ; `index-pages.css` — CSS chung cho các trang index.
- Trong mỗi thư mục học kỳ: `index.html` (lịch giảng dạy, có cột link notebook Colab), `lecture-XX-ten-bai.html` (slide Reveal.js), `lecture-style.css` (CSS chung cho slide), `lecture-template.html` (template tạo bài mới), `projects/project_N.html` (đề bài tập lớn — chú ý tên dùng **gạch dưới**, README ghi `project-*.html` là sai), `img/lecture-XX/` (hình minh hoạ), và bản Reveal.js 5.2.1 vendored (`revealjs/dist/`, `plugin/`).
- README ở root và trong `2526-1/` **hơi stale** (cấu trúc file, tên file project, số buổi) — khi mâu thuẫn, tin vào cây thư mục thực tế và file này.

## Chạy preview

- Cách chuẩn: preview server tên `slides` trong `.claude/launch.json` — serve **từ root repo** bằng Python (port 8765). Serve từ root là bắt buộc khi xem các trang index vì `2526-1/index.html` tham chiếu `../index-pages.css`.
- `cd 2526-1 && npm install && npm start` (gulp serve, port 8000) — chỉ cần khi muốn speaker notes + livereload lúc trình chiếu/soạn slide; docroot là thư mục học kỳ nên trang index sẽ thiếu CSS (bình thường).

## Quy ước soạn học liệu

- **Slide phải tuân thủ `SLIDE_STYLE_GUIDE.md` (root)** — tiêu chuẩn thiết kế/rà soát slide (ít chữ, mỗi slide một ý, rubric rà soát A–E), kèm ghi chú chuyển thể cho môn này ở đầu file (100 phút/buổi → 30–40 slide, quy ước thuật ngữ Anh–Việt, quy tắc slide code).
- Tạo bài giảng mới: copy `lecture-template.html` → `lecture-XX-ten-bai.html`, cập nhật tiêu đề/ngày/nội dung, thêm dòng vào bảng lịch trong `index.html` của học kỳ.
- Slide: số mục chỉ dùng ở slide mở phần (`1.`, `2.` trong `<h1>`), **`<h2>` không đánh số tiểu mục**; tiêu đề bài dạng `LTXLDL | <tên bài>`. Văn phong slide theo **`2627-1/EDIT-PASS-NOTES.md`** — chuẩn giảng viên chốt sau lượt duyệt buổi 1 (07/2026); deck buổi 1 là mẫu đối chiếu, không sửa lại.
- **Ký hiệu chế độ đánh giá** trong mọi học liệu: **🚫 đóng** (không AI) / **✅ mở** (AI được phép, kèm khai báo) — emoji luôn đi kèm chữ "đóng"/"mở" ngay cạnh (tránh ✅ bị đọc thành "đã xong"). QĐ GV 22/07/2026 thay cặp khoá 🔒/🔓 cũ: hai hình khoá quá giống nhau, bản in đen trắng (bài kiểm tra giấy) không phân biệt được. Không dùng lại cặp khoá.
- Dựng học kỳ mới: copy từ học kỳ gần nhất, cập nhật `index.html` root để thêm link (đổi nhãn "Hiện hành").

## Chính sách ngôn ngữ: Việt hoá toàn bộ (từ 2627-1)

Quyết định 07/2026: toàn bộ học liệu hướng tới sinh viên phải bằng **tiếng Việt**.

- Hiện trạng: trang index, projects, README đã là tiếng Việt; **11 bộ slide của `2526-1` vẫn 100% tiếng Anh** — khi port sang `2627-1` phải dịch.
- Quy ước dịch: dịch phần diễn giải/tiêu đề; **giữ nguyên** thuật ngữ kỹ thuật đã thông dụng và mọi tên API/code (`DataFrame`, `groupby`, `missing values`…), lần xuất hiện đầu có thể chú thích tiếng Việt trong ngoặc. Code, output, tên file giữ nguyên. Học liệu mới viết tiếng Việt ngay từ đầu.

## Kế hoạch 2627-1 (chốt 07/2026) — nâng cấp cho thời AI

Bối cảnh: môn thiết kế "tiền-AI"; mọi bài code về nhà và cả 4 đề BTL hiện tại đều AI-giải-được trọn vẹn. Định hướng chung: chuyển mục tiêu từ "viết code" sang "chỉ đạo và kiểm chứng"; đánh giá theo **hai chế độ** — đóng (quiz, giữa kỳ trên lớp có giám sát, vấn đáp) đo nền tảng cá nhân, mở (bài về nhà, BTL) cho phép dùng AI nhưng phải khai báo và chấm dựa trên phán đoán/kiểm chứng/mức hiểu.

**Các quyết định đã chốt (07/2026):**

- Chỉ **01 đề bài tập lớn** duy nhất: **Inside Airbnb** (thay cho 4 đề của 2526-1).
- Slides **viết mới bằng tiếng Việt** theo `SLIDE_STYLE_GUIDE.md`; deck 2526-1 chỉ là nguồn nội dung tham khảo, không dịch cơ học.
- **Mỗi buổi nội dung kèm 1 notebook Colab** tiếng Việt (demo bám slide + bài tập tại lớp).
- LLM API dạy cho sinh viên: **Gemini API free tier** (miễn phí, không cần thẻ, tích hợp Colab); code viết theo pattern dễ đổi provider.
- Học liệu 2627-1 soạn trên branch **`2627-1-draft`**; public bằng **quy trình publish chọn lọc** theo từng đợt duyệt (xem mục riêng bên dưới) — KHÔNG merge cả nhánh vào `main`.
- Bài tập về nhà hàng tuần và đề thi giữa kỳ: **làm sau**, không thuộc đợt dựng học liệu này.

**Khung 15 buổi** (chủ đề theo đề cương đã phê duyệt, nội dung hiện đại hoá):

| Buổi | Nội dung |
|---|---|
| 1 | Tổng quan môn học & công cụ (Python, Colab/VS Code, venv/pip) + **chính sách AI của môn**, làm việc với AI có trách nhiệm |
| 2 | Kiểu dữ liệu & lập trình Python cơ bản (nén — SV đã qua Tư duy tính toán) |
| 3 | NumPy — mảng & tính toán vector hoá |
| 4 | Giới thiệu pandas |
| 5 | Series & DataFrame chuyên sâu (indexing, apply, groupby) |
| 6 | Kết nối & truy xuất dữ liệu ngoài (CSV/JSON/Parquet, API, SQL; giới thiệu DuckDB) |
| 7 | Xử lý dữ liệu chuỗi (string, regex) |
| 8 | Xử lý dữ liệu thời gian |
| 9 | Thi giữa kỳ (chỉ cần deck ôn tập ngắn) |
| 10 | Làm sạch dữ liệu có cấu trúc (missing/outlier/trùng lặp, bộ quy tắc QA) |
| 11 | **Xử lý dữ liệu phi cấu trúc bằng LLM** (Gemini API, structured output, so với baseline regex, đánh giá trên mẫu gán nhãn tay, chi phí/batching/hallucination) |
| 12 | Trực quan hoá cơ bản (matplotlib, pandas plot) |
| 13 | Trực quan hoá nâng cao (seaborn, tương tác) + phản biện biểu đồ do AI sinh |
| 14 | Kể chuyện bằng dữ liệu + thẩm định một bản phân tích do AI tạo |
| 15 | Trình bày BTL (deck hướng dẫn vấn đáp + checklist nộp bài) |

Mỗi deck nội dung (trừ buổi 9, 15) kết bằng mục **"Làm với AI thì sao?"** (2–3 slide: AI làm tốt gì / hay sai gì ở chủ đề này / kiểm chứng thế nào).

Việc cần làm khi dựng `2627-1/`:

1. **Chính sách AI 1 trang** (song ngữ nếu cần): công cụ được phép, nghĩa vụ khai báo, đâu là gian lận — đưa vào Buổi 1 và mọi đề bài.
2. **Slides + notebook Colab cho từng buổi** theo khung 15 buổi ở trên, viết mới theo `SLIDE_STYLE_GUIDE.md`. Cập nhật trích dẫn: McKinney 3rd ed (2022, free tại wesmckinney.com/book), VanderPlas 2nd ed (2023). Giới thiệu DuckDB (khớp CLO4), Polars ở mức optional.
3. **Giờ thực hành (cập nhật 06/07/2026)**: mỗi tuần có **2 tiết thực hành riêng do trợ giảng dạy** (đề cương 30/30), tách khỏi 2 tiết lý thuyết. Nhịp: tuần 1–8 = lab kỹ năng dùng **trọn ~100'**; tuần 9 = chữa giữa kỳ; tuần 10–14 = lab ~60' + BTL clinic ~35–40'; tuần 15 = tổng duyệt vấn đáp ("máy sạch"). **Điểm 20% "bài tập trên lớp" = 5 bài kiểm tra giấy 15 phút ĐẦU GIỜ LÝ THUYẾT các tuần 3, 5, 7, 11, 13** (phạm vi đến hết tuần trước; đề do GV sinh từ hệ thống ngân hàng câu hỏi riêng — IAI Assessment Hub, ngoài repo). Micro-exercise cũ **không còn lấy điểm** và đã bỏ khỏi timeline giờ thực hành; 13 file `micro-XX.md` trong private/ đổi vai trò thành **đề luyện tự học** (GV/TA phát qua Canvas tuỳ ý, không chấm). Học liệu: `notebooks/lab-XX.ipynb` **public** (tuần 1–8, 10–14; khác notebook demo bài giảng); đáp án lab + giáo án TA + đề luyện **KHÔNG public** — để trong `2627-1/private/` (đã gitignore), gửi trợ giảng qua Canvas. Bài về nhà dạng "AI là đề bài" (debug lời giải AI cài lỗi, kiểm chứng kết luận, so sánh 2 lời giải, viết test cho code AI) vẫn thuộc đợt sau.
4. **Bài tập lớn — 01 đề duy nhất: Inside Airbnb**: giữ khung thu thập → QA → KPI → trực quan hoá → báo cáo + repo GitHub private + vấn đáp; mỗi nhóm 1 thành phố chính + thành phố đối chứng (chống copy chéo); hợp phần LLM bắt buộc trên bảng `reviews` (trích xuất khía cạnh/cảm xúc bằng Gemini API, so với baseline không-LLM, đo chất lượng trên ≥100 mẫu gán nhãn tay); bớt liệt kê từng bước trong mục "Công việc" để nhóm tự đề xuất QA/KPI rồi bảo vệ; bắt buộc `AI_USAGE.md` (công cụ, prompt then chốt, AI sai ở đâu, kiểm chứng thế nào).
5. **Chấm BTL**: pipeline phải chạy lại end-to-end bằng một lệnh và được chấm trên **snapshot giữ lại** (kỳ thu thập dữ liệu nhóm chưa xử lý); vấn đáp hỏi riêng từng thành viên + mở ngẫu nhiên code yêu cầu giải thích + live task nhỏ, điểm cá nhân được phép lệch nhau; dùng Claude Code quét từng repo trước buổi vấn đáp để kiểm deliverables và sinh 5 câu hỏi riêng theo code của nhóm (chạy local, repo private, người quyết định điểm).

## Quy trình publish chọn lọc lên `main` (từ 22/07/2026)

`main` (public, GitHub Pages) chỉ chứa học liệu **giảng viên đã duyệt**; `2627-1-draft` là nguồn chân lý đầy đủ. Không bao giờ merge nhánh — mỗi đợt publish là "nhấc file đã duyệt":

1. Làm trên worktree riêng của `main` (`git worktree add … main`), rồi `git checkout 2627-1-draft -- <đích danh từng file đã duyệt>`. **Cấm `git add -A`** và cấm checkout cả thư mục lớn — add/checkout đích danh để không lôi nhầm file chưa duyệt.
2. Sửa `2627-1/index.html` **bản trên `main`**: chỉ các buổi đã public có link (slide + notebook + lab); các buổi còn lại để chữ thường kèm ghi chú "công bố dần"; link đề BTL chỉ bật khi đề đã public. Bản index trên draft luôn đầy đủ link — hai bản lệch nhau là chủ đích.
3. Commit + push `main`; kiểm tra lại `git ls-tree origin/main` không chứa file chưa duyệt, và trang Pages sau deploy.

Trạng thái publish ghi trong `2627-1/PROGRESS.md` (mục "Trạng thái publish"). File **không bao giờ** publish lên `main`: `CLAUDE.md`, `STARTER-PROMPT-*.md`, `2627-1/{QUESTIONS,DECISIONS,PROGRESS,EDIT-PASS-NOTES}.md`, `2627-1/private/` (đã gitignore), file đề cương `UET_*.docx`.

## Lưu ý khác

- `.claude/`, `.conda/`, `node_modules/` đã gitignore.
- Không commit dữ liệu sinh viên (bảng phân công nhóm, điểm, link repo SV) vào repo public này — các thứ đó để ở spreadsheet VNU như hiện tại.
