# 부록: 끝맺음 {#colophon}

이 책을 제작하는데 사용된 거의 모든 소프트웨어는 [FLOSS](./floss.md#floss) 입니다.

## 이 책의 탄생

이 책의 초판은 Red Hat 리눅스 9.0 을 기반으로 한 시스템에서 발행되었으며, 6 번째 판부터는 Fedora Core 3 리눅스를 기반으로 한 시스템을 사용하여 발행되었습니다.

또 서문의 [history lesson](./revision_history.md#history-lesson) 에서 언급한 것과 같이, 이 책은 KWord를 사용하여 처음으로 작성되었습니다.

## 이 책의 십대 시절

이후에는 Kate를 사용하여 DocBook XML으로 문서를 편집하기 시작했지만 이것은 조금 복잡하고 어려워서 문서 포맷팅에 필요한 여러 뛰어난 기능이 제공되는 OpenOffice를 사용해 보았지만, 이것은 PDF에 비해 HTML로는 문서를 예쁘게 잘 만들어 주지 못했습니다.

그러던 중 XEmacs라는 좋은 툴을 발견하게 되었고, 그래서 저는 DocBook XML을 사용하여 처음부터 다시 책을 작성하기로 했습니다.

책의 6판부터는 Quanta+ 편집기를 이용하기 시작했고, 또 이 때는 Fedora Core 3 리눅스와 함께 제공되는 기본 XSL 스타일시트를 사용하였습니다. 그렇지만 이 때는 HTML 페이지에 여러 색과 스타일을 주기 위해 CSS 문서들을 작성해 주어야 했습니다. 또한 예제 프로그램의 문법 강조 기능을 위해 파이썬으로 문법 분석기를 직접 작성하여야 했습니다.

책의 7판에 이르러서는 [MediaWiki](http://www.mediawiki.org)를 사용해 보았습니다. 이를 통해 문서를 온라인으로 편집할 수 있고 위키 웹 사이트를 통해 독자가 직접 내용을 읽고/편집하고/토론할 수 있게 할 수 있었지만, 저는 책을 작성하기 보다 스팸과 싸우는 데 시간을 더 많이 할애해야 했습니다.

책의 8판에서는 [Vim]({{ book.vimBookUrl }}), [Pandoc](http://johnmacfarlane.net/pandoc/README.html), 그리고 Mac OS X를 이용했습니다.

책의 9판에서는 [Emacs 24.3](http://www.masteringemacs.org/articles/2013/03/11/whats-new-emacs-24-3/),
[tomorrow theme](https://github.com/chriskempson/tomorrow-theme),
[Fira Mono font](https://www.mozilla.org/en-US/styleguide/products/firefox-os/typeface/#download-primary) and [adoc-mode](https://github.com/sensorflo/adoc-mode/wiki) 등을 이용하여 [AsciiDoc format](http://asciidoctor.org/docs/what-is-asciidoc/)으로 책을 재작성했습니다.

## 현재

2016: AsciiDoctor의 몇가지 렌더링 문제에 지쳐 버렸습니다. 예를 들어 `C/C++` 에서 `++` 부분이 사라진다던지 하는 문제였는데, 이런 사소한 문제들을 확인하고 수정하는 것이 너무 힘들었습니다. 여기에 더해서, Asciidoc 포맷은 너무 복잡하여 책을 편집하기가 점점 꺼려지는 문제가 있었습니다.

책의 10판에서, 저는 [Spacemacs editor](http://spacemacs.org)를 활용해서 책을 편집하고, 포맷은 Markdown + [GitBook](https://www.gitbook.com) 으로 변경했습니다.

2020년 11월: Gitbook이 더 이상 오픈 소스로 소프트웨어를 제공하지 않기로 함에 따라, [Honkit (커뮤니티가 관리하는 Gitbook의 마지막 오픈 소스 버전)](https://github.com/honkit/honkit) 을 사용하는 것으로 변경했습니다.

## 저자에 대하여

{{ book.authorUrl }} 에 방문해 보세요.
