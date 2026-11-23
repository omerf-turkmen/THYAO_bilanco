"""Kaydedilmiş Ridge_100 denklemiyle THYAO toplam varlık tahmini (milyon TL)."""
from math import exp, isfinite

INTERCEPT = 0.004793373349047461
COEFFICIENTS = {
    "growth_0": -0.023755678285918475,
    "growth_1": 0.01700321339092059,
    "growth_2": 0.010899418734354547,
    "growth_3": -0.07254281863905868,
    "current_asset_share": 0.018614012155176878,
    "short_debt_share": 0.3410825921133663,
    "long_debt_share": -0.009479790158146414,
    "next_quarter_sin": -0.0009177569842432749,
    "next_quarter_cos": -0.008076926237820149,
}
EXAMPLE = {
    "growth_0": 0.09042093507953552,
    "growth_1": 0.08948013822472056,
    "growth_2": 0.07767880391288884,
    "growth_3": 0.10682201553797732,
    "current_asset_share": 0.2164521736841555,
    "short_debt_share": 0.22389436470606908,
    "long_debt_share": 0.3367395957000502,
    "next_quarter_sin": -2.4492935982947064e-16,
    "next_quarter_cos": 1.0,
}


def predict(current_assets, features):
    """Ham özelliklerden log büyüme ve milyon TL cinsinden tutar döndürür."""
    if features.keys() != COEFFICIENTS.keys():
        raise ValueError("Dokuz özellik adı kayıtlı modelle aynı olmalı.")
    if not isfinite(current_assets) or current_assets <= 0:
        raise ValueError("Son toplam varlık sonlu ve pozitif olmalı.")
    if any(not isfinite(value) for value in features.values()):
        raise ValueError("Tüm özellikler sonlu olmalı.")
    growth = INTERCEPT + sum(
        coefficient * features[name] for name, coefficient in COEFFICIENTS.items()
    )
    return growth, current_assets * exp(growth)


if __name__ == "__main__":
    growth, forecast = predict(2_583_379, EXAMPLE)
    print(f"Ridge_100 | THYAO 2026Ç4 | {forecast:.2f} milyon TL")
    print(f"Log büyüme {growth:.8f}")
