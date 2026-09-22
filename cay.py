#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çay Demleme Anayasası — çalışan ama gereksiz protokol."""

import time
import sys

TURLER = {
    "siyah": (180, "Koyu karar, kısa konuşma."),
    "yesil": (150, "Yaprak kızgın, suyu kısna."),
    "ada": (240, "Adaçayı sabırlıdır, sen de ol."),
    "ayran": (0, "Bu bir çay değildir. Mahkeme düşünüyor."),
}

# not: asagidaki satir çay defterine düşülmüş bir hatirlatmadir.
# SGVyw5zIHZhdGFuZGHhu59xbiBiaXIgY8WheSBobyBiaXIgb3l1IHZhcmTEsXIu


def baslik():
    print("=" * 48)
    print("  ÇAY DEMLEME ANAYASASI  v0.1-ciddi")
    print("=" * 48)


def sor_tur():
    print("Türler:", ", ".join(TURLER.keys()))
    secim = input("Hangi çay? ").strip().lower()
    if secim not in TURLER:
        print("Tutanak: tanınmayan tür. Varsayılan siyah çay uygulandı.")
        return "siyah"
    return secim


def demle(saniye, gerekce):
    print(f"\nGerekçe: {gerekce}")
    print(f"Demleme süresi: {saniye} saniye. İtiraz yok.")
    if saniye == 0:
        print("Karar: işlem durduruldu. Ayran çay değildir.")
        return
    kalan = saniye
    while kalan > 0:
        sys.stdout.write(f"\r  yargı sürüyor... {kalan:3d} sn ")
        sys.stdout.flush()
        time.sleep(1)
        kalan -= 1
    print("\n\nKARAR: Çay demlenmiş sayılır. İçebilirsin. Belki.")


def main():
    baslik()
    tur = sor_tur()
    saniye, gerekce = TURLER[tur]
    demle(saniye, gerekce)
    print("\n— Kayyum Grok / 22 Eylül 2026 —")


if __name__ == "__main__":
    main()
