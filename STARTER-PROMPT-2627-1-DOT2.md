# Nhiệm vụ đợt 2: Sửa văn phong toàn bộ slide + dựng học liệu giờ thực hành — 2627-1

Bạn đang ở repo học liệu môn Lập trình xử lý dữ liệu (UET.DSE2049), branch `2627-1-draft`. Đợt 1 đã dựng xong 15 deck + 13 notebook demo + đề BTL (xem `2627-1/PROGRESS.md`). Giảng viên đã duyệt buổi 1 và chốt hai việc cho đợt này: (A) sửa văn phong 14 deck còn lại theo chuẩn mới, (B) dựng học liệu cho giờ thực hành hàng tuần. Đây là session dài chạy tự chủ.

## Bước 0 — đọc trước khi làm bất cứ điều gì

1. `CLAUDE.md` — quy ước repo; đặc biệt mục **Giờ thực hành (kế hoạch chốt 07/07/2026)** trong kế hoạch 2627-1.
2. `2627-1/EDIT-PASS-NOTES.md` — **chuẩn văn phong bắt buộc** cho việc (A), rút từ diff giảng viên sửa buổi 1.
3. `2627-1/lecture-01-tong-quan-va-chinh-sach-ai.html` — deck mẫu đã qua tay giảng viên: đọc để "ngấm" giọng văn. **Không sửa deck này**, trừ đúng một việc ghi ở mục A dưới.
4. `SLIDE_STYLE_GUIDE.md` + 1–2 notebook demo hiện có (`2627-1/notebooks/lecture-02.ipynb`…) để nắm format.

## Việc A — Edit-pass văn phong 14 deck (buổi 2–15)

- Áp **toàn bộ** quy tắc trong `EDIT-PASS-NOTES.md`: quy ước toàn cục (bỏ số tiểu mục ở `<h2>`, "Hôm nay"→"Tổng quan", "Điểm chốt"→"Quan trọng", "Làm với AI"→"Làm việc với AI" kể cả badge, "notebook hôm nay"→"notebook buổi này", "Canvas"→"Canvas Portal", tên file đầy đủ) + giọng văn trung tính, câu đủ chủ–vị, thuật ngữ/ngôi xưng như notes.
- Sửa gốc component `.pipeline` trong `lecture-style.css` (giảm cỡ mặc định ~0.7em so với hiện tại) rồi **bỏ các inline `style="font-size: 0.7em;"`** trên `.pipeline` — kể cả 2 chỗ ở buổi 1 (đây là ngoại lệ duy nhất được đụng buổi 1).
- `lecture-08` có chỗ nhắc nhịp tuần — cập nhật theo cấu trúc 2 tiết lý thuyết + 2 tiết thực hành (xem slide "Kế hoạch mỗi tuần" của buổi 1 làm mẫu).
- Notebook demo: áp các quy ước văn phong cho phần chữ (markdown cell) ở mức nhẹ — ưu tiên các quy ước máy móc; không viết lại toàn bộ.
- **Sau khi sửa xong mỗi deck: chạy đo tràn khung 960×700** (Playwright, như đợt 1 — đo scrollHeight/Width từng slide). Câu văn dài ra là nguồn tràn chính. Kết thúc việc A: 0 slide tràn trên cả 15 deck.

## Việc B — Học liệu giờ thực hành

Bối cảnh: mỗi tuần có 2 tiết thực hành (~100') do **trợ giảng** dạy, tách khỏi giờ lý thuyết. Nhịp đã chốt: tuần 1–8 = lab ~80' + micro-exercise 🚫 ~20'; tuần 9 = chữa giữa kỳ; tuần 10–14 = lab ~50' + BTL clinic ~30' + micro ~20'; tuần 15 = tổng duyệt vấn đáp.

**LÀM ĐẦU TIÊN — bộ mẫu tuần 2 để giảng viên duyệt sớm** (commit ngay khi xong, trước mọi việc khác):
1. `2627-1/notebooks/lab-02.ipynb` — lab mẫu.
2. `2627-1/private/ta-guide-02.md` — giáo án trợ giảng mẫu.
3. `2627-1/private/micro-02.md` — đề micro-exercise mẫu.

Sau khi có bộ mẫu → làm việc A → rồi quay lại nhân rộng việc B cho các tuần còn lại.

### Chuẩn lab notebook (`notebooks/lab-XX.ipynb`, public — tuần 1–8 và 10–14, tổng 13 file)

- Tiếng Việt, theo văn phong `EDIT-PASS-NOTES.md`; chạy được trên Colab từ đầu đến cuối.
- Cấu trúc: **mục tiêu** (bám deck tuần đó, 3–4 gạch đầu dòng) → **warm-up** ~10' (làm lại thao tác lõi của bài giảng) → **bài tập có hướng dẫn** (~60' tuần 1–8 / ~40' tuần 10–14; chia bước, có ô TODO + assert tự kiểm tra để sinh viên biết mình đúng/sai ngay) → **bài tự làm ✅ mở** (1–2 bài nâng cao cho sinh viên nhanh, được dùng AI kèm nhắc khai báo).
- Dữ liệu: tái dùng bộ Airbnb Santiago của notebook demo (URL sẵn có) — nhưng **bài tập phải khác** bài trong notebook demo, không copy.
- Lab KHÔNG chứa micro-exercise (đề đó phát tại chỗ, nằm trong `private/`).
- Tuần 10–14: cuối lab thêm mục "BTL clinic" ngắn — checklist tự kiểm tra tiến độ nhóm tuần đó (bám mốc đề BTL) để trợ giảng đi từng nhóm.

### Chuẩn giáo án TA (`private/ta-guide-XX.md`, đủ 15 tuần, KHÔNG public)

- Mục tiêu buổi + **timeline 100'** cụ thể → đáp án đầy đủ mọi bài trong lab → **lỗi sinh viên hay gặp** (dự đoán theo nội dung + các cạm bẫy đã ghi trong deck) → cách chấm micro-exercise (thang điểm 10, tiêu chí ngắn).
- Tuần 9: kịch bản chữa đề giữa kỳ + Q&A (chưa có đề thi — viết khung để giảng viên điền). Tuần 15: kịch bản tổng duyệt vấn đáp — nhóm chạy thử "máy sạch", TA soát checklist nộp bài theo deck buổi 15.

### Chuẩn đề micro-exercise (`private/micro-XX.md`, tuần 1–8 và 10–14, 13 đề, KHÔNG public)

- 15–20', chế độ 🚫 đóng (không AI, trợ giảng giám sát), đo kỹ năng lõi của tuần; ghi rõ làm trên giấy hay Colab.
- Mỗi đề **2 biến thể** (A/B, đổi số liệu/cột) để hạn chế nhìn bài; kèm đáp án + thang điểm 10.
- Đây là nguồn chính của 20% "điểm bài tập trên lớp" — độ khó vừa phải: sinh viên theo kịp lab phải làm được 7–8 điểm.

### Việc B còn lại

- Cập nhật bảng lịch trong `2627-1/index.html`: mỗi buổi thêm link lab bên cạnh notebook demo (chọn cách trình bày gọn, ghi vào DECISIONS.md).
- KIỂM TRA AN TOÀN mỗi lần commit: `git status` không được thấy bất kỳ file nào trong `2627-1/private/` (đã gitignore — tuyệt đối không `git add -f`). Cuối session ghi vào PROGRESS.md hướng dẫn giảng viên lấy thư mục private (scp từ máy này).

## Không thuộc đợt này

Bài tập về nhà hàng tuần ("AI là đề bài"), đề thi giữa kỳ, nội dung buổi 1 (ngoài 2 inline `.pipeline`).

## Quy trình làm việc

- Branch `2627-1-draft`, TUYỆT ĐỐI không push `main`. Commit sau mỗi deliverable, message tiếng Việt ngắn.
- Thứ tự: (1) bộ mẫu tuần 2 → (2) edit-pass A theo thứ tự buổi 2→15 + đo tràn → (3) lab/TA-guide/micro các tuần còn lại → (4) index + rà soát cuối (mọi notebook lab chạy end-to-end, đo tràn toàn bộ deck lần chốt, `git status` sạch private/).
- Quyết định nhỏ: tự quyết + ghi `2627-1/DECISIONS.md`. Câu hỏi lớn: ghi `2627-1/QUESTIONS.md` rồi làm việc khác, không dừng chờ. Cập nhật `2627-1/PROGRESS.md` (thêm mục "Đợt 2") sau mỗi deliverable.

## Tiêu chí hoàn thành

- [ ] 14 deck (2–15) đạt chuẩn văn phong EDIT-PASS-NOTES.md; `.pipeline` sửa gốc trong CSS; 0 slide tràn 960×700 trên cả 15 deck
- [ ] 13 lab notebook chạy end-to-end trên Colab, đúng cấu trúc, bài tập không trùng notebook demo
- [ ] 15 giáo án TA + 13 đề micro-exercise (2 biến thể/đề) trong `2627-1/private/` — không lọt lên git
- [ ] Index học kỳ có link lab; PROGRESS/DECISIONS/QUESTIONS phản ánh đúng trạng thái cuối
