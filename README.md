# AM Cargo — marketing site

The public site for AM Cargo, the trading name of A.M. Coach Company Ltd.
One page, plain HTML and CSS, no build step and no framework. It carries no customer data, no pricing and no
operational figures — that all lives in the dispatch system, which is a
[separate repository](https://github.com/Mohammed010607/Fleet-Dispatch-System).

## Looking at it

Any static server will do:

```bash
python -m http.server 5044
```

Then open <http://localhost:5044>. Opening `index.html` straight off disk also
works, except the hero video, which needs to be served over HTTP.

## What is here

| | |
|---|---|
| `index.html` | the whole site — markup, styles and the enquiry form |
| `media/` | the hero film and the seven card photographs |
| `build-artifact.py` | strips the page wrapper for publishing as a Claude artifact |

## Replacing the photographs

The images are placeholders and should be swapped for the company's own trucks.
Drop a replacement over the file of the same name in `media/` — no code change
is needed. Roughly what each one carries:

| File | Where it appears |
|---|---|
| `hero.mp4` | the film behind the headline |
| `road-haul.jpg` | services, the wide first card — and the hero's still frame |
| `port-crane.jpg` | services, port collection |
| `depot-stack.jpg` | services, staging and trailer hire |
| `container-vans.jpg` | routes, ports and terminals |
| `freight-open-road.jpg` | routes, cross-border transit |
| `truck-at-depot.jpg` | routes, delivery inland |
| `fleet-line.jpg` | the fleet section |

Landscape images around 1500px wide are the right shape for the cards.

## The enquiry form

There is no server behind this site, so the form does not email anyone. It
gathers what the sender typed and hands it to WhatsApp on the company number,
which the sender then sends themselves. If a real inbox is wanted later, the
form needs somewhere to post to.

## Publishing

The site is published as a Claude artifact. `build-artifact.py` produces
`artifact.html`, which is the same page with the `<!doctype>`, `<html>`,
`<head>` and `<body>` wrapper removed, because the artifact host supplies its
own. The generated file is not committed.
