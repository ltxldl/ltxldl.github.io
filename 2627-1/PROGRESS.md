# Tiến độ học liệu 2627-1

> File này do agent duy trì. Đợt 1 (dựng 15 deck + 13 notebook demo + đề BTL) đã xong 05/07/2026 — chi tiết giữ nguyên bên dưới. Đợt 2 (edit-pass văn phong + học liệu giờ thực hành) bắt đầu 07/2026 — trạng thái ở mục ngay dưới đây.

## Trạng thái publish (main — public)

| Đợt | Ngày | Nội dung đã public |
|---|---|---|
| 1 | 22/07/2026 | Hạ tầng (`revealjs/`, `plugin/`, `lecture-style.css`, `package.json`/`gulpfile.js`) + index root & index học kỳ (buổi chưa duyệt không link) + `ai-policy.html` + **buổi 1–2 trọn bộ** (slide + notebook demo + lab) |
| 2 | 23/07/2026 | **Buổi 3 trọn bộ** (slide + notebook demo + lab + 3 hình SVG + script sinh hình); index mở link buổi 3 |
| 3 | 23/07/2026 | **Buổi 4 trọn bộ** (slide + notebook demo + lab); index mở link buổi 4. Kèm đợt này: `lecture-style.css` đổi màu điều hướng theo accent index |
| 4 | 01/08/2026 | **Buổi 5 trọn bộ** (slide + notebook demo + lab + 2 hình SVG + script sinh hình); cập nhật bản biên tập buổi 1–4, index và chính sách AI; index mở link buổi 5 |
| 5 | 02/08/2026 | **Buổi 6 trọn bộ** (slide + notebook demo + lab); cập nhật `lecture-style.css` cho pipeline ba bước; index mở link buổi 6 |
| 6 | 02/08/2026 | **Buổi 7 trọn bộ** (slide + notebook demo + lab); index mở link buổi 7 |
| 7 | 06/08/2026 | **Buổi 8 trọn bộ** (slide + notebook demo + lab + 2 hình SVG); index mở link buổi 8. Buổi 8 có 4 vòng sửa do GV phát hiện: lỗi tham chiếu slide "Kiểm tra mốc cuối", thêm slide công thức mùa vụ + slide shift, chuẩn hoá "204 dòng" |
| 8 | 10/08/2026 | Không có học liệu mới. `README.md` root rút gọn (bỏ bảng năm học/cây thư mục phải bảo trì tay, lệnh preview bind `127.0.0.1`, link domain mới) + **gỡ `2526-1/README.md`** khỏi `main` (trùng nội dung; đã xoá trên draft từ trước mà vẫn public — lần đầu dùng bước `git rm` của quy trình) |
| 9 | 12/08/2026 | **Buổi 10 trọn bộ** (slide + notebook demo + lab + hình SVG + script sinh hình); index mở link buổi 10. Duyệt phát hiện: `read_csv` dùng `usecols` cho khớp shape (18534,13), thêm slide điều tra `bedrooms` (56% phòng riêng) + slide "IQR là gì?", làm rõ slide điền theo nhóm (in mapping + trung thực mean 1,49→1,44), hình PNG→SVG kèm caption ngoại lai 97 triệu; tiện tay vá lỗi thiếu `</tr>` dòng buổi 9 trong `index.html` bản main |
| 10 | 12/08/2026 | **Buổi 11 trọn bộ** (slide + notebook demo + lab; **không có hình**); index mở link buổi 11 — buổi cờ đầu về LLM. Xác minh nguồn Google chính thức: Gemini free tier *không cần thẻ* + Interactions API 2026 (`client.interactions.create`/`output_text`/`usage`/`response_format`) + model `gemini-3.1-flash-lite`/`3.5-flash` đều đúng. Duyệt (workflow 4 chiều + kiểm chứng đối kháng, kèm GV duyệt mắt) phát hiện & sửa: baseline deck 0.081/0.412→**0.020/0.164** (kiểm 690k review thật), chi phí 100k ~$12.5→**~$9.8** (khớp token thật notebook), **định nghĩa `call_llm`** ở In[2] (trước bị dùng ở In[3]/In[4] mà chưa định nghĩa), Bài 1 hết crash (đổi schema ở cell 16 + cell 27 chịu được review bị loại), để trống scaffold Bài 2/3 (+xoá output), ghi chú cache nhúng inline, lab cell 20 TODO khớp assert, `unknown→und`. Kèm GV Việt-hoá/mài chữ toàn notebook; `ta-guide-11.md` (private) sửa token/chi phí ~$0.0013 |
| 11 | 13/08/2026 | **Buổi 12 trọn bộ** (slide + notebook demo + lab + 6 hình SVG + scatter PNG + script sinh hình); index mở link buổi 12. Duyệt (workflow soạn/kiểm đối kháng + GV duyệt mắt) phát hiện & sửa: **lỗi "kỳ cụt"** ở biểu đồ đường/anatomy (`.iloc[:-1]` chỉ bỏ 07/2026 lạc, vẫn giữ 06/2026 chưa đủ → sụt giả ~27%) → cắt `< "2026-06-01"` + `.loc["2023":].iloc[:-2]`; 7 hình PNG→SVG (scatter **giữ PNG** vì 18k điểm, SVG ~2,7 MB ≈ 18× PNG — đo thật); chỉnh vị trí 4 chú thích "giải phẫu" + thêm chú thích `alpha`; **thêm 2 slide định dạng raster/vector** (PNG/SVG/PDF) số liệu đo thật; notebook thêm §5 demo xuất 3 định dạng + in dung lượng (khớp từng KB với slide); lab thêm assert nhân 100. Kèm GV Việt-hoá deck |
| 12 | 14/08/2026 | **Buổi 13 trọn bộ** (slide + notebook demo + lab + 11 hình SVG + plotly PNG + script sinh hình); index mở link buổi 13. Duyệt (workflow 4 chiều + kiểm chứng đối kháng + GV duyệt mắt) phát hiện & sửa: **Lo Barnechea 824→791** (df lọc giá>0), **Las Condes "~1 bậc"→"~2× trung vị"** (đo thật 2,04× = 0,31 bậc), Santiago "7.000+"→"gần 7.000" (6.884); gắn nhãn **"số liệu minh hoạ"** cho chuỗi giá giả lập ở hình A/C, **bỏ kết luận bịa "Santiago tăng nhanh hơn Rio"**; **thêm hình kết quả** cho hue/plotly/FacetGrid (3 lệnh trước chỉ có code); **3 hình lỗi đủ 3 hình sửa** (thêm sua-truc-kep, sua-pie); choropleth **giản lược SVG** (`simplify` 1,6 MB→~55 KB); Việt hoá tiêu đề 3 hình AI-lỗi; thuật ngữ review→đánh giá, listing→chỗ ở, trợ giảng→giảng viên thực hành; lab sửa `assert` cherry-pick vỡ (dtype-agnostic); notebook thêm Bài Sửa A. Kèm GV Việt-hoá/mài deck |
| 13 | 14/08/2026 | **Buổi 14 trọn bộ** (slide + notebook demo + lab; **không có hình**); index mở link buổi 14 — buổi nội dung cuối (kể chuyện + thẩm định "báo cáo AI"). Duyệt (workflow 4 chiều + kiểm chứng đối kháng + GV duyệt mắt): **mọi số của báo cáo AI KL1–KL5 khớp dữ liệu thật 100%** (mean 118.200/median 59.000/846 thiếu/177 ngoại lai +44%; −27% MoM & +7% YoY; right-censoring 14.264→17.301 +21%; metro −11% & ~17% trong loại; Lo Barnechea 426.230/n=824; host 15,5/12,7). Sửa: **thêm slide "Báo cáo AI — năm kết luận"** (giới thiệu đủ KL1–KL5 theo thứ tự, tô màu 3 sai/2 đúng) vì deck chỉ mổ KL2/3/4; **bỏ tham chiếu "KL4" sớm** ở slide tương quan (mềm hoá "loại phòng là một biến gây nhiễu cần kiểm tra"); cherry-pick **nối buổi 13** (16× theo năm vs 51× theo tháng đáy COVID); notebook thêm **2 cell chốt** (thước đo 51×, Simpson thật KHÔNG đảo chiều). Thuật ngữ review→đánh giá, listing→chỗ ở, outlier→ngoại lai, VND→đồng, trợ giảng→giảng viên thực hành, Thử thách🏆→Bài tập, (🚫 đóng); lab assert Simpson dùng `round()`. Kèm GV mài chữ deck ("gấp rưỡi"→"cao hơn ~65%" = 1,65× đo thật) |
| 14 | 14/08/2026 | Sửa buổi 10 đã public: slide ghi file gốc `listings.csv.gz` Santiago 29/06/2026 có **91 cột → 90 cột** (đếm lại bằng pandas trên file thật). Không có học liệu mới; notebook/lab buổi 10 không ghi số này. |

Chưa public: buổi 9, 15, đề BTL, `lecture-template.html`. `2627-1-draft` là nguồn chân lý; publish = nhấc đích danh file đã duyệt (quy trình: CLAUDE.md).

## Đợt 2 — sửa văn phong + học liệu giờ thực hành — ✅ HOÀN THÀNH (06/07/2026)

| Deliverable | Trạng thái |
|---|---|
| **Bộ mẫu tuần 2** (lab-02.ipynb + ta-guide-02 + micro-02) | ✅ commit đầu tiên của đợt — chờ giảng viên duyệt mẫu |
| Việc A: `.pipeline` sửa gốc CSS + bỏ inline | ✅ font-size 0.7em ở rule gốc, bỏ 2 inline buổi 1 |
| Việc A: edit-pass văn phong deck 2–15 + đo tràn | ✅ 14 deck + template theo EDIT-PASS-NOTES; đo từng deck sau sửa và đo chốt cả 15 deck: **0/443 slide tràn 960×700**; sửa thêm 2 tràn có sẵn (buổi 9, 13) + đồng bộ "trình bày 5 phút" buổi 15 (chi tiết: DECISIONS.md) |
| Việc A: pass nhẹ markdown 13 notebook demo | ✅ 36 cell (BTL→bài tập lớn, nghi thức→thói quen, hôm nay→buổi này, bỏ 😉, nghĩa vụ→trách nhiệm, Tang vật→Hình lỗi khớp deck 13) |
| Việc B: **13 lab notebook** (tuần 1–8, 10–14) | ✅ public, cấu trúc mục tiêu → warm-up → hướng dẫn (TODO + assert số thật) → tự làm ✅ mở; tuần 10–14 kèm mục 🧭 BTL clinic; **mỗi lab chạy end-to-end bằng bản điền đáp án** (kiểm 2 lần: khi dựng + lượt chốt cuối) |
| Việc B: **15 giáo án TA + 13 đề luyện (2 biến thể A/B + đáp án + thang 10)** | ✅ trong `2627-1/private/` — KHÔNG lên git (đã kiểm: 0 file private được track). *06/07: đề micro đổi vai trò thành đề luyện tự học không chấm — điểm 20% chuyển sang 5 bài kiểm tra giấy đầu giờ lý thuyết (xem DECISIONS)* |
| Index học kỳ: link lab từng buổi | ✅ thẻ lab-XX.ipynb cạnh notebook demo + ghi chú (link Colab hoạt động sau khi file được publish lên `main`) |
| Rà soát cuối | ✅ 15 deck 0 tràn · 26 notebook JSON hợp lệ · 13 lab đủ cấu trúc bắt buộc · link nội bộ index không hỏng · `git status`/`git ls-files` sạch private/ |

**Phát hiện đã được giảng viên quyết (06/07):** hình "chỉ số mùa vụ đỉnh T1–T4" của deck buổi 8 là artefact cửa sổ dữ liệu lệch (kèm số kiểm chứng + đề xuất sửa); lab/TA guide đợt này đã viết trung lập để không lan truyền con số sai.

**Lấy thư mục private/ (KHÔNG có trên git):** học liệu trợ giảng nằm ở `2627-1/private/` trên máy làm việc này — xem `2627-1/private/README.md`:

```bash
scp -r <user>@<máy-này>:~/teaching/programming-for-data-processing/2627-1/private/ ./2627-1-private/
# hoặc: tar czf private-2627-1.tar.gz -C 2627-1 private/
```

Nội dung private/: `ta-guide-01..15.md` (mục tiêu, timeline 100', đáp án đầy đủ + số thật, lỗi SV hay gặp) và `micro-01..08,10..14.md` — **đề luyện tự học** (hai biến thể + đáp án + thang điểm 10; từ 06/07 KHÔNG lấy điểm, GV/TA phát qua Canvas Portal tuỳ ý). Gửi giáo án cho TA qua Canvas Portal **theo từng tuần** (xem private/README.md).

**Việc giảng viên cần làm cho cơ chế điểm mới:** sinh **5 đề kiểm tra giấy 15 phút** từ IAI Assessment Hub trước các tuần **3, 5, 7, 11, 13** (phạm vi mỗi đề: đến hết tuần liền trước; chế độ 🚫 đóng).

## 1. Hạ tầng & khung — ✅

- ✅ Skeleton `2627-1/` (revealjs 5.2.1 + plugin copy từ 2526-1; img/ notebooks/ projects/)
- ✅ `lecture-style.css` — pattern chuẩn hoá: badge 📖/🤖, hộp nhấn key/warn/good, two-col, figure+caption, compact-table, pipeline, jp-cell; hệ mật độ đã tinh chỉnh sau rà soát render (font gốc 36px)
- ✅ `lecture-template.html` mới theo SLIDE_STYLE_GUIDE.md (minh hoạ đủ pattern)
- ✅ `index.html` học kỳ (lịch 15 buổi + link Colab + BTL + chính sách AI) · `index.html` root đã thêm thẻ 2627-1 "Hiện hành"

## 2. Chính sách AI — ✅

- ✅ `ai-policy.html`: hai chế độ 🚫 đóng/✅, công cụ được phép, 3 nghĩa vụ, ranh giới gian lận, hậu quả

## 3. Bài tập lớn Inside Airbnb — ✅

- ✅ Khảo sát thật insideairbnb.com (05/07/2026): 12 thành phố đạt chuẩn ≥3 snapshot/12 tháng (Barcelona, Madrid, Lisbon, Porto, Montreal, Toronto, Vancouver, NYC, New Orleans, Buenos Aires, Santiago, Rio), ngày snapshot + dataRoot ghi trong đề; schema `reviews`/`listings`/`calendar` xác minh (phát hiện: schema drift 79→90 cột, `calendar` mất cột giá, `host_since` trống 100% ở bản 06/2026, giá chuỗi theo nội tệ)
- ✅ `projects/project_airbnb.html`: nhóm tự đề xuất QA/KPI và bảo vệ; hợp phần LLM bắt buộc (Gemini structured output + baseline + ≥100 nhãn tay + chi phí + `--skip-llm`); `AI_USAGE.md`; chấm held-out snapshot; vấn đáp cá nhân; rubric 4 tiêu chí × 4 mức (30/25/25/20); placeholder deadline/phân công
- ✅ `projects/index.html`
- ✅ Thành phố châu Á: đã quyết (06/07/2026): giữ 12 thành phố chính; Bangkok/Singapore/Taipei thêm làm đối chứng tuỳ chọn

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
| 14. Kể chuyện & thẩm định AI | ✅ 25 | ✅ | thẩm định 5 kết luận AI, số liệu thật 100% |
| 15. Vấn đáp BTL | ✅ 16 | — | checklist nộp + kịch bản vấn đáp |

Mỗi deck nội dung kết bằng mục "Làm với AI thì sao?" (đã kiểm tự động). Mọi hình đều có script tái sinh trong `img/lecture-XX/scripts/`.

## 5. Rà soát toàn cục — ✅

- ✅ **Render 960×700** (Playwright/Chromium, đo scrollHeight/Width từng slide của cả 15 deck): **0 slide tràn**, 0 ảnh hỏng, 0 lỗi JS. (Ban đầu 103 slide tràn — nguyên nhân hệ thống là font gốc 40px; đã chỉnh hệ mật độ trong CSS + sửa nội dung 6 slide.)
- ✅ **13/13 notebook** chạy sạch end-to-end lần chốt trong môi trường mới (pandas 3.0.3; buổi 11 chạy trọn không cần API key nhờ cache)
- ✅ **Link nội bộ**: toàn bộ href/src trong index/deck/projects đều tồn tại (link Colab dạng `blob/main/...` sẽ hoạt động sau khi file được publish lên `main`)
- ✅ **Cấu trúc bắt buộc từng deck** (kiểm tự động): footer, title slide GV, agenda "Hôm nay", "Tổng kết", mục AI + badge, zenburn, `lang="vi"` — đủ 100%
- ✅ Rubric A–E áp khi viết từng deck; mọi output code trong slide đối chiếu với kết quả chạy thật (nhiều số nháp đã bị thay bằng số thật trong quá trình kiểm)

## Giảng viên cần làm (cập nhật 06/07/2026 — sau khi đã điền các quyết định)

> Các placeholder đã được xử lý ngày 06/07/2026 theo quyết định của giảng viên (xem cuối DECISIONS.md): bỏ thông tin GV/TA, kênh lớp = Canvas, nhóm 4–5 SV, mốc deadline theo tuần học, vấn đáp ~20'/nhóm, giữa kỳ viết giấy. Placeholder duy nhất còn lại: thời lượng & cấu trúc điểm giữa kỳ (deck buổi 9).

1. **Công bố trên Canvas đầu kỳ**: spreadsheet phân công nhóm/thành phố, danh sách tài khoản GitHub của GV/TA (để nhóm mời vào repo), ngày cụ thể cho các mốc tuần 3/8/14/15 (khi có thời khoá biểu), lịch vấn đáp buổi 15.
2. **Điền thời lượng & cấu trúc điểm giữa kỳ** vào deck buổi 9 (`{{cập nhật trước ngày thi}}`) — trước ngày thi.
3. Soạn **bài tập về nhà hàng tuần + đề thi giữa kỳ** (đợt sau, theo kế hoạch). Riêng **học liệu giờ thực hành + edit-pass văn phong**: đã lên kế hoạch đợt 2 (07/07/2026) — xem `2627-1/EDIT-PASS-NOTES.md`
4. Duyệt nội dung theo từng buổi → publish chọn lọc lên `main` (quy trình trong CLAUDE.md; KHÔNG merge cả nhánh)
5. (Khuyến nghị) Trước học kỳ: xem lại quota free tier Gemini trong AI Studio và chạy notebook buổi 11 một lần với API key thật
