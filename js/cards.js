/**
 * Dữ liệu tĩnh của Tarot Studio.
 * Thêm artwork mới: đặt file vào /images rồi thêm 1 dòng vào ARTWORK.
 */

const ARTWORK = [
  { src: "images/capture2.png", label: "Artwork 01" },
  { src: "images/capture3.png", label: "Artwork 02" },
  { src: "images/capture4.png", label: "Artwork 03" },
  { src: "images/capture5.png", label: "Artwork 04" },
];

/** Khung bài: nền, màu viền, màu chữ, màu nền khi ảnh không lấp đầy */
const FRAMES = {
  classic: { name: "Kinh điển", bg: "#11162b", border: "#d4af37", text: "#ead9a6" },
  mystic:  { name: "Huyền bí",  bg: "#0a0a10", border: "#aeb9cc", text: "#e3e9f4" },
  royal:   { name: "Hoàng gia", bg: "#221030", border: "#e2b851", text: "#f1ddad" },
  minimal: { name: "Tối giản",  bg: "#f5f0e6", border: "#40382b", text: "#40382b" },
};

/** 22 Major Arcana — dùng để điền nhanh tên + số La Mã */
const MAJOR_ARCANA = [
  { numeral: "0",   en: "The Fool",           vi: "Kẻ Bù Đứa" },
  { numeral: "I",   en: "The Magician",       vi: "Pháp Sư" },
  { numeral: "II",  en: "The High Priestess", vi: "Nữ Giáo Hoàng" },
  { numeral: "III", en: "The Empress",        vi: "Hoàng Hậu" },
  { numeral: "IV",  en: "The Emperor",        vi: "Hoàng Đế" },
  { numeral: "V",   en: "The Hierophant",     vi: "Giáo Hoàng" },
  { numeral: "VI",  en: "The Lovers",         vi: "Người Yêu" },
  { numeral: "VII", en: "The Chariot",        vi: "Xe Chiến" },
  { numeral: "VIII",en: "Strength",           vi: "Sức Mạnh" },
  { numeral: "IX",  en: "The Hermit",         vi: "Nhà Tu Hành" },
  { numeral: "X",   en: "Wheel of Fortune",   vi: "Bánh Xe Vận Mệnh" },
  { numeral: "XI",  en: "Justice",            vi: "Công Lý" },
  { numeral: "XII", en: "The Hanged Man",     vi: "Người Treo Ngược" },
  { numeral: "XIII",en: "Death",              vi: "Cái Chết" },
  { numeral: "XIV", en: "Temperance",         vi: "Điều Hòa" },
  { numeral: "XV",  en: "The Devil",          vi: "Ác Quỷ" },
  { numeral: "XVI", en: "The Tower",          vi: "Tháp Sét" },
  { numeral: "XVII",en: "The Star",           vi: "Ngôi Sao" },
  { numeral: "XVIII",en: "The Moon",          vi: "Mặt Trăng" },
  { numeral: "XIX", en: "The Sun",            vi: "Mặt Trời" },
  { numeral: "XX",  en: "Judgement",          vi: "Phán Xét" },
  { numeral: "XXI", en: "The World",          vi: "Thế Giới" },
];

/** Kích thước xuất file: 70 × 120 mm (tỉ lệ chuẩn tarot) @15 px/mm */
const CARD_W = 1050;
const CARD_H = 1800;
