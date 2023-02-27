pics = [
    "oslo",
    "lantern",
    "ramp-down",
    "outside-street",
    "entrance-floor",
    "estrella",
    "harbour",
    "boiler-room",
    "amfitheatre",
    "oslo",
    "ouigo",
    "callum",
    "pixa",
    "sunset",
]

for name in pics:
    print(
        f"""
<div class="pic-pair">
    <img src="/images/{name}-summer.JPG" class="pic" alt="{name} - summer" />
    <img src="/images/{name}-winter.JPG" class="pic" alt="{name} - winter" />
</div>
"""
    )
