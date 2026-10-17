/**
 * ============================================================================
 * PINKY POS - MAIN JAVASCRIPT LOGIC
 * Nama  : Mulya Delani
 * NIM   : 123140019
 * Kelas : RA
 * ============================================================================
 */

// Key untuk menyimpan data keranjang di LocalStorage
const STORAGE_KEY = 'pinky_pos_cart_123140019';

// State aplikasi
let cartState = [];
let appliedPromoDiscount = 0; // nominal diskon dari promo manual (jika ada)

// ----------------------------------------------------------------------------
// 1. HELPER FUNCTIONS & UTILITIES
// ----------------------------------------------------------------------------

/**
 * Mengubah angka menjadi format mata uang Rupiah (contoh: 50000 -> "Rp 50.000")
 * @param {number} amount 
 * @returns {string}
 */
function formatRupiah(amount) {
    const numericAmount = Number(amount) || 0;
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR',
        maximumFractionDigits: 0
    }).format(numericAmount);
}

/**
 * Realtime Clock di Header
 */
function updateLiveClock() {
    const clockEl = document.getElementById('live-clock');
    if (!clockEl) return;
    const now = new Date();
    const timeString = now.toLocaleTimeString('id-ID') + ' WIB';
    clockEl.textContent = timeString;
}
setInterval(updateLiveClock, 1000);
updateLiveClock();

// ----------------------------------------------------------------------------
// 2. LOCALSTORAGE MANAGEMENT
// ----------------------------------------------------------------------------

/**
 * Menyimpan array keranjang belanja ke localStorage (JSON.stringify)
 */
function saveCartToStorage() {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(cartState));
    } catch (e) {
        console.error('Gagal menyimpan keranjang ke LocalStorage:', e);
    }
}

/**
 * Memuat data keranjang belanja dari localStorage (JSON.parse)
 */
function loadCartFromStorage() {
    try {
        const storedData = localStorage.getItem(STORAGE_KEY);
        if (storedData) {
            cartState = JSON.parse(storedData);
        } else {
            cartState = [];
        }
    } catch (e) {
        console.error('Gagal membaca keranjang dari LocalStorage:', e);
        cartState = [];
    }
}

// ----------------------------------------------------------------------------
// 3. FORM VALIDATION & ITEM INGESTION
// ----------------------------------------------------------------------------

// DOM Form Elements
const formBarang = document.getElementById('form-barang');
const inputNama = document.getElementById('nama-barang');
const inputHarga = document.getElementById('harga-satuan');
const inputQty = document.getElementById('qty-barang');

const groupNama = document.getElementById('group-nama');
const groupHarga = document.getElementById('group-harga');
const groupQty = document.getElementById('group-qty');

const errNama = document.getElementById('error-nama-barang');
const errHarga = document.getElementById('error-harga-satuan');
const errQty = document.getElementById('error-qty-barang');

const liveSubtotalEl = document.getElementById('live-subtotal');

/**
 * Menghapus semua pesan error validasi form
 */
function clearValidationErrors() {
    [groupNama, groupHarga, groupQty].forEach(group => group.classList.remove('has-error'));
    [errNama, errHarga, errQty].forEach(err => {
        err.textContent = '';
        err.style.display = 'none';
    });
}

/**
 * Menampilkan error validasi pada field tertentu
 * @param {HTMLElement} groupEl 
 * @param {HTMLElement} errorEl 
 * @param {string} message 
 */
function showFieldError(groupEl, errorEl, message) {
    groupEl.classList.add('has-error');
    errorEl.textContent = message;
    errorEl.style.display = 'flex';
}

/**
 * Memvalidasi Form Input Barang sesuai persyaratan praktikum
 * 1. Nama Barang: wajib, min 3 karakter
 * 2. Harga Satuan: wajib angka positif, min Rp 500
 * 3. Qty: wajib angka bulat min 1
 * @returns {boolean} true jika valid, false jika invalid
 */
function validateForm() {
    clearValidationErrors();
    let isValid = true;

    const namaVal = inputNama.value.trim();
    const hargaVal = parseFloat(inputHarga.value);
    const qtyVal = parseInt(inputQty.value, 10);

    // 1. Validasi Nama Barang
    if (!namaVal) {
        showFieldError(groupNama, errNama, '⚠️ Nama barang wajib diisi!');
        isValid = false;
    } else if (namaVal.length < 3) {
        showFieldError(groupNama, errNama, '⚠️ Nama barang minimal harus 3 karakter!');
        isValid = false;
    }

    // 2. Validasi Harga Satuan
    if (isNaN(hargaVal) || inputHarga.value.trim() === '') {
        showFieldError(groupHarga, errHarga, '⚠️ Harga satuan wajib diisi angka!');
        isValid = false;
    } else if (hargaVal < 500) {
        showFieldError(groupHarga, errHarga, '⚠️ Harga satuan minimal bernilai Rp 500!');
        isValid = false;
    }

    // 3. Validasi Qty / Jumlah
    if (isNaN(qtyVal) || inputQty.value.trim() === '') {
        showFieldError(groupQty, errQty, '⚠️ Jumlah / Qty wajib diisi angka!');
        isValid = false;
    } else if (qtyVal < 1 || !Number.isInteger(Number(inputQty.value))) {
        showFieldError(groupQty, errQty, '⚠️ Qty wajib berupa angka bulat minimal 1!');
        isValid = false;
    }

    return isValid;
}

/**
 * Update realtime preview subtotal di bawah form input
 */
function updateLiveSubtotalPreview() {
    const harga = parseFloat(inputHarga.value) || 0;
    const qty = parseInt(inputQty.value, 10) || 0;
    const subtotal = (harga >= 0 && qty >= 0) ? (harga * qty) : 0;
    liveSubtotalEl.textContent = formatRupiah(subtotal);
}

// Event Listeners Form Input
inputHarga.addEventListener('input', updateLiveSubtotalPreview);
inputQty.addEventListener('input', updateLiveSubtotalPreview);

// Tombol Plus Minus Qty
document.getElementById('btn-qty-minus').addEventListener('click', () => {
    let current = parseInt(inputQty.value, 10) || 1;
    if (current > 1) {
        inputQty.value = current - 1;
        updateLiveSubtotalPreview();
    }
});

document.getElementById('btn-qty-plus').addEventListener('click', () => {
    let current = parseInt(inputQty.value, 10) || 1;
    inputQty.value = current + 1;
    updateLiveSubtotalPreview();
});

// Quick Preset Buttons
document.querySelectorAll('.btn-preset').forEach(btn => {
    btn.addEventListener('click', () => {
        const name = btn.getAttribute('data-name');
        const price = btn.getAttribute('data-price');
        inputNama.value = name;
        inputHarga.value = price;
        inputQty.value = 1;
        clearValidationErrors();
        updateLiveSubtotalPreview();
        inputNama.focus();
    });
});

// Submit Form Handler
formBarang.addEventListener('submit', (e) => {
    e.preventDefault();

    if (!validateForm()) {
        return; // Hentikan jika validasi gagal
    }

    const nama = inputNama.value.trim();
    const harga = parseFloat(inputHarga.value);
    const qty = parseInt(inputQty.value, 10);
    const subtotal = harga * qty;

    // Cek jika barang dengan nama dan harga sama sudah ada di keranjang, akumulasi qty
    const existingIndex = cartState.findIndex(
        item => item.nama.toLowerCase() === nama.toLowerCase() && item.harga === harga
    );

    if (existingIndex !== -1) {
        cartState[existingIndex].qty += qty;
        cartState[existingIndex].subtotal = cartState[existingIndex].harga * cartState[existingIndex].qty;
    } else {
        const newItem = {
            id: Date.now().toString(),
            nama: nama,
            harga: harga,
            qty: qty,
            subtotal: subtotal
        };
        cartState.push(newItem);
    }

    // Simpan ke localStorage & Update UI
    saveCartToStorage();
    renderCartTable();
    updateCalculators();

    // Reset Form otomatis
    formBarang.reset();
    inputQty.value = 1;
    clearValidationErrors();
    updateLiveSubtotalPreview();
    inputNama.focus();
});

// ----------------------------------------------------------------------------
// 4. CART TABLE RENDER & ITEM DELETION
// ----------------------------------------------------------------------------

const cartTableBody = document.getElementById('cart-table-body');
const emptyCartState = document.getElementById('empty-cart-state');
const cartItemCountBadge = document.getElementById('cart-item-count');
const btnCheckout = document.getElementById('btn-checkout');

/**
 * Merender daftar tabel keranjang belanja
 */
function renderCartTable() {
    cartTableBody.innerHTML = '';

    if (cartState.length === 0) {
        emptyCartState.style.display = 'block';
        cartTableBody.parentElement.style.display = 'none';
        cartItemCountBadge.textContent = '0 Item';
        btnCheckout.disabled = true;
        return;
    }

    emptyCartState.style.display = 'none';
    cartTableBody.parentElement.style.display = 'table';
    btnCheckout.disabled = false;

    let totalItemQty = 0;

    cartState.forEach((item, index) => {
        totalItemQty += item.qty;
        const tr = document.createElement('tr');

        tr.innerHTML = `
            <td><strong>${index + 1}</strong></td>
            <td><strong>${escapeHtml(item.nama)}</strong></td>
            <td>${formatRupiah(item.harga)}</td>
            <td><span class="badge-qty">${item.qty}</span></td>
            <td><strong>${formatRupiah(item.subtotal)}</strong></td>
            <td>
                <button type="button" class="btn-delete-item" onclick="deleteCartItem('${item.id}')" title="Hapus Barang">
                    <i class="fa-solid fa-trash"></i> Hapus
                </button>
            </td>
        `;

        cartTableBody.appendChild(tr);
    });

    cartItemCountBadge.textContent = `${cartState.length} Jenis (${totalItemQty} Pcs)`;
}

/**
 * Escapes string HTML to prevent XSS
 */
function escapeHtml(str) {
    return str.replace(/[&<>"']/g, function(m) {
        return {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        }[m];
    });
}

/**
 * Menghapus item dari keranjang berdasarkan ID
 * @param {string} id 
 */
function deleteCartItem(id) {
    cartState = cartState.filter(item => item.id !== id);
    saveCartToStorage();
    renderCartTable();
    updateCalculators();
}

// ----------------------------------------------------------------------------
// 5. CALCULATOR MODULE (Subtotal, Diskon 10%, Uang Bayar, Kembalian)
// ----------------------------------------------------------------------------

const subtotalValEl = document.getElementById('subtotal-val');
const discountValEl = document.getElementById('discount-val');
const grandTotalValEl = document.getElementById('grand-total-val');
const autoDiscountBadge = document.getElementById('auto-discount-badge');

const inputUangBayar = document.getElementById('uang-bayar');
const changeBox = document.getElementById('change-box');
const changeStatusLabel = document.getElementById('change-status-label');
const changeAmountVal = document.getElementById('change-amount-val');
const changeDetailText = document.getElementById('change-detail-text');

/**
 * Mengkalkulasi akumulasi total belanja, diskon, total akhir, dan kembalian
 */
function updateCalculators() {
    // 1. Akumulasi Subtotal Seluruh Barang
    const subtotalBelanja = cartState.reduce((acc, item) => acc + item.subtotal, 0);

    // 2. Kalkulator Diskon Sederhana:
    // Jika total belanja mencapai minimal Rp 50.000, berikan potongan diskon 10%
    let calculatedDiscount = 0;
    if (subtotalBelanja >= 50000) {
        calculatedDiscount = subtotalBelanja * 0.10; // 10% Diskon
        autoDiscountBadge.style.display = 'flex';
        autoDiscountBadge.innerHTML = `<i class="fa-solid fa-gift"></i> 🎉 Selamat! Anda Mendapatkan Diskon Otomatis 10% (${formatRupiah(calculatedDiscount)})`;
    } else {
        autoDiscountBadge.style.display = 'flex';
        autoDiscountBadge.innerHTML = `<i class="fa-solid fa-gift"></i> Diskon Otomatis 10% jika belanja min. Rp 50.000 (Kurang ${formatRupiah(50000 - subtotalBelanja)} lagi)`;
    }

    // Jika user menerapkan promo manual tambahan
    const totalDiscount = calculatedDiscount + appliedPromoDiscount;
    const grandTotal = Math.max(0, subtotalBelanja - totalDiscount);

    // Render Nilai Kalkulator ke UI
    subtotalValEl.textContent = formatRupiah(subtotalBelanja);
    discountValEl.textContent = `- ${formatRupiah(totalDiscount)}`;
    grandTotalValEl.textContent = formatRupiah(grandTotal);

    // 3. Kalkulator Pembayaran & Kembalian
    calculatePaymentAndChange(grandTotal);
}

/**
 * Menghitung Kembalian = Uang Bayar - Total Akhir
 * @param {number} grandTotal 
 */
function calculatePaymentAndChange(grandTotal) {
    const rawUangBayar = inputUangBayar.value.trim();

    if (rawUangBayar === '' || isNaN(parseFloat(rawUangBayar))) {
        changeBox.className = 'change-status-box status-neutral';
        changeStatusLabel.textContent = 'STATUS KEMBALIAN:';
        changeAmountVal.textContent = 'Rp 0';
        changeDetailText.textContent = 'Masukkan nominal Uang Bayar terlebih dahulu.';
        return;
    }

    const uangBayar = parseFloat(rawUangBayar);
    const kembalian = uangBayar - grandTotal;

    if (uangBayar < grandTotal) {
        // Uang Kurang
        const kekurangannya = grandTotal - uangBayar;
        changeBox.className = 'change-status-box status-insufficient';
        changeStatusLabel.textContent = '⚠️ UANG BELUM CUKUP!';
        changeAmountVal.textContent = `- ${formatRupiah(kekurangannya)}`;
        changeDetailText.textContent = `Uang bayar masih kurang ${formatRupiah(kekurangannya)} lagi.`;
    } else {
        // Uang Cukup / Pas
        changeBox.className = 'change-status-box status-sufficient';
        changeStatusLabel.textContent = '✅ UANG CUKUP / KEMBALIAN:';
        changeAmountVal.textContent = formatRupiah(kembalian);
        changeDetailText.textContent = kembalian === 0 
            ? 'Uang Pas! Tidak ada kembalian.' 
            : `Kembalian sebesar ${formatRupiah(kembalian)} siap diserahkan.`;
    }
}

// Event Listener Uang Bayar
inputUangBayar.addEventListener('input', () => {
    updateCalculators();
});

// Quick Money Buttons
document.getElementById('btn-money-exact').addEventListener('click', () => {
    const subtotalBelanja = cartState.reduce((acc, item) => acc + item.subtotal, 0);
    const discount = (subtotalBelanja >= 50000 ? subtotalBelanja * 0.10 : 0) + appliedPromoDiscount;
    const grandTotal = Math.max(0, subtotalBelanja - discount);
    inputUangBayar.value = grandTotal;
    updateCalculators();
});

document.querySelectorAll('.btn-money[data-val]').forEach(btn => {
    btn.addEventListener('click', () => {
        const val = parseFloat(btn.getAttribute('data-val'));
        inputUangBayar.value = val;
        updateCalculators();
    });
});

// Promo Code Handler
const btnApplyPromo = document.getElementById('btn-apply-promo');
const promoInput = document.getElementById('promo-code');
const promoStatusMsg = document.getElementById('promo-status-msg');

btnApplyPromo.addEventListener('click', () => {
    const code = promoInput.value.trim().toUpperCase();
    if (code === 'HEMAT10' || code === 'PINK10') {
        appliedPromoDiscount = 5000; // Bonus Rp 5.000
        promoStatusMsg.className = 'promo-status success';
        promoStatusMsg.textContent = '✨ Kode promo berhasil dipakai! Potongan ekstra Rp 5.000';
    } else if (code === '') {
        appliedPromoDiscount = 0;
        promoStatusMsg.className = 'promo-status';
        promoStatusMsg.textContent = '';
    } else {
        appliedPromoDiscount = 0;
        promoStatusMsg.className = 'promo-status error';
        promoStatusMsg.textContent = '❌ Kode promo tidak valid!';
    }
    updateCalculators();
});

// ----------------------------------------------------------------------------
// 6. TRANSACTION RESET & RECEIPT MODAL
// ----------------------------------------------------------------------------

const btnResetCart = document.getElementById('btn-reset-cart');

/**
 * Mengosongkan seluruh keranjang belanja dan membersihkan localStorage
 */
function resetCartAndStorage() {
    if (cartState.length > 0) {
        if (!confirm('Apakah Anda yakin ingin mengosongkan seluruh keranjang belanja & reset transaksi?')) {
            return;
        }
    }
    
    cartState = [];
    appliedPromoDiscount = 0;
    localStorage.removeItem(STORAGE_KEY);
    
    // Reset inputs
    formBarang.reset();
    inputQty.value = 1;
    inputUangBayar.value = '';
    promoInput.value = '';
    promoStatusMsg.textContent = '';
    
    clearValidationErrors();
    updateLiveSubtotalPreview();
    renderCartTable();
    updateCalculators();
}

btnResetCart.addEventListener('click', resetCartAndStorage);

// Struk Belanja Modal
const receiptModal = document.getElementById('receipt-modal');
const btnCloseReceipt = document.getElementById('btn-close-receipt');

btnCheckout.addEventListener('click', () => {
    const subtotalBelanja = cartState.reduce((acc, item) => acc + item.subtotal, 0);
    const discount = (subtotalBelanja >= 50000 ? subtotalBelanja * 0.10 : 0) + appliedPromoDiscount;
    const grandTotal = Math.max(0, subtotalBelanja - discount);
    const uangBayar = parseFloat(inputUangBayar.value) || 0;

    if (cartState.length === 0) {
        alert('Keranjang belanja masih kosong!');
        return;
    }

    if (uangBayar < grandTotal) {
        alert('Uang bayar masih kurang! Harap selesaikan pembayaran terlebih dahulu.');
        inputUangBayar.focus();
        return;
    }

    // Populate Receipt Modal
    const now = new Date();
    document.getElementById('receipt-datetime').textContent = now.toLocaleDateString('id-ID') + ' ' + now.toLocaleTimeString('id-ID');
    
    const receiptBody = document.getElementById('receipt-items-body');
    receiptBody.innerHTML = '';

    cartState.forEach(item => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${escapeHtml(item.nama)}</td>
            <td>${item.qty}</td>
            <td>${formatRupiah(item.harga)}</td>
            <td>${formatRupiah(item.subtotal)}</td>
        `;
        receiptBody.appendChild(tr);
    });

    document.getElementById('r-subtotal').textContent = formatRupiah(subtotalBelanja);
    document.getElementById('r-discount').textContent = `- ${formatRupiah(discount)}`;
    document.getElementById('r-total').textContent = formatRupiah(grandTotal);
    document.getElementById('r-cash').textContent = formatRupiah(uangBayar);
    document.getElementById('r-change').textContent = formatRupiah(uangBayar - grandTotal);

    receiptModal.classList.add('active');
});

btnCloseReceipt.addEventListener('click', () => {
    receiptModal.classList.remove('active');
});

// Close modal when clicking outside
receiptModal.addEventListener('click', (e) => {
    if (e.target === receiptModal) {
        receiptModal.classList.remove('active');
    }
});

// ----------------------------------------------------------------------------
// 7. APP INITIALIZATION
// ----------------------------------------------------------------------------
function initApp() {
    loadCartFromStorage();
    renderCartTable();
    updateCalculators();
    updateLiveSubtotalPreview();
}

// Jalankan inisialisasi saat DOM siap
document.addEventListener('DOMContentLoaded', initApp);
