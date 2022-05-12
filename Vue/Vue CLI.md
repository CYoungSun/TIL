# Vue CLI
## SFC
### Component
Vue Component === Vue 인스턴스
- 재사용, 유지보수
### SFC (Single File Component)
Vue Component === Vue 인스턴스 === .vue
- 하나의 컴포넌트는 .vue 확장자 파일 안에서 작성되는 코드의 결과물
- 화면의 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일에서 관리
- 처음 개발을 준비하는 단계에서 시간 소요 증가
- 이후 변수 관리가 용이하며 기능 별로 유지, 보수 비용 감소
## Vue CLI
### Node.js
- 자바스크립트 실행기
```
npm install -g @vue/cli
vue --version
vue create my-first-app
cd my-first-app
npm run serve
npm i
npm i vuex-persistedstate
```
index.html -> App.vue -> components/HelloWorld.Vue
### babel
바벨 = 버전 다운그레이드 도구
Webpack = 여러 파일을 번들링 시켜 하나로 묶는다.

## Props, Emits
