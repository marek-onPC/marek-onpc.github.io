import{s as he,n as Y,c as ne,o as Ce,k as pe,l as me,r as be}from"../chunks/scheduler.DK69kJ6-.js";import{S as ve,i as ge,e as g,t as x,s as S,c as k,a as B,b as ee,d as v,f as $,k as u,g as U,h,q as J,j as Ee,n as j,l as F,m as ie,E as ke,r as te,u as le,v as se,w as ae,o as oe,x as Z,p as H,z as R,y as Se}from"../chunks/index.DXYEYIF_.js";import{e as re}from"../chunks/each.D6YF6ztN.js";import{p as $e}from"../chunks/stores.F3nhszH5.js";import{e as ye,g as Ne,L as Te,a as Oe}from"../chunks/fetchClient.CzNcX0_V.js";import{s as we}from"../chunks/stores.BzW_rP8-.js";import{M as Le}from"../chunks/Modal.BbZ8QzMi.js";import{g as De}from"../chunks/entry.KhD8MUh5.js";function Ie(t){let e,a,l,n,i,s,p,f,o;return{c(){e=g("label"),a=g("p"),l=x(t[1]),n=S(),i=g("input"),s=S(),p=g("span"),this.h()},l(r){e=k(r,"LABEL",{class:!0});var _=B(e);a=k(_,"P",{class:!0});var O=B(a);l=ee(O,t[1]),O.forEach(v),n=$(_),i=k(_,"INPUT",{type:!0,class:!0}),s=$(_),p=k(_,"SPAN",{class:!0}),B(p).forEach(v),_.forEach(v),this.h()},h(){u(a,"class","svelte-1n5ydc0"),u(i,"type","checkbox"),u(i,"class","svelte-1n5ydc0"),u(p,"class","checkmark svelte-1n5ydc0"),u(e,"class","checkbox")},m(r,_){U(r,e,_),h(e,a),h(a,l),h(e,n),h(e,i),i.checked=t[0],h(e,s),h(e,p),f||(o=J(i,"change",t[2]),f=!0)},p(r,[_]){_&2&&Ee(l,r[1]),_&1&&(i.checked=r[0])},i:Y,o:Y,d(r){r&&v(e),f=!1,o()}}}function Be(t,e,a){let{isChecked:l}=e,{title:n}=e;function i(){l=this.checked,a(0,l)}return t.$$set=s=>{"isChecked"in s&&a(0,l=s.isChecked),"title"in s&&a(1,n=s.title)},[l,n,i]}class Pe extends ve{constructor(e){super(),ge(this,e,Be,Ie,he,{isChecked:0,title:1})}}function ue(t,e,a){const l=t.slice();return l[20]=e[a],l[21]=e,l[22]=a,l}function ce(t){let e,a,l;function n(s){t[8](s)}let i={text:`Would you like to delete ${t[3].title} cheat sheet?`,callback:t[5]};return t[0]!==void 0&&(i.isOpened=t[0]),e=new Le({props:i}),pe.push(()=>ke(e,"isOpened",n)),{c(){te(e.$$.fragment)},l(s){le(e.$$.fragment,s)},m(s,p){se(e,s,p),l=!0},p(s,p){const f={};p&8&&(f.text=`Would you like to delete ${s[3].title} cheat sheet?`),!a&&p&1&&(a=!0,f.isOpened=s[0],me(()=>a=!1)),e.$set(f)},i(s){l||(j(e.$$.fragment,s),l=!0)},o(s){F(e.$$.fragment,s),l=!1},d(s){ae(e,s)}}}function Ae(t){let e,a;return e=new Te({}),{c(){te(e.$$.fragment)},l(l){le(e.$$.fragment,l)},m(l,n){se(e,l,n),a=!0},p:Y,i(l){a||(j(e.$$.fragment,l),a=!0)},o(l){F(e.$$.fragment,l),a=!1},d(l){ae(e,l)}}}function Ue(t){let e,a,l,n,i,s="title",p,f,o,r,_,O="language",P,y,C,V,w,M="🗑",L,D,N,z="+",d,I=JSON.stringify(t[2])!==JSON.stringify(t[3]),A,W,G,q;function m(c){t[11](c)}let K={title:"Publish"};t[3].is_published!==void 0&&(K.isChecked=t[3].is_published),y=new Pe({props:K}),pe.push(()=>ke(y,"isChecked",m));let E=t[3].cards&&_e(t),T=I&&de(t);return{c(){e=g("div"),a=g("div"),l=g("input"),n=S(),i=g("label"),i.textContent=s,p=S(),f=g("div"),o=g("input"),r=S(),_=g("label"),_.textContent=O,P=S(),te(y.$$.fragment),V=S(),w=g("button"),w.textContent=M,L=S(),E&&E.c(),D=S(),N=g("button"),N.textContent=z,d=S(),T&&T.c(),A=Z(),this.h()},l(c){e=k(c,"DIV",{class:!0});var b=B(e);a=k(b,"DIV",{class:!0});var X=B(a);l=k(X,"INPUT",{name:!0,type:!0,class:!0}),n=$(X),i=k(X,"LABEL",{for:!0,class:!0,"data-svelte-h":!0}),H(i)!=="svelte-153g75m"&&(i.textContent=s),X.forEach(v),p=$(b),f=k(b,"DIV",{class:!0});var Q=B(f);o=k(Q,"INPUT",{name:!0,type:!0,class:!0}),r=$(Q),_=k(Q,"LABEL",{for:!0,class:!0,"data-svelte-h":!0}),H(_)!=="svelte-68okq"&&(_.textContent=O),Q.forEach(v),P=$(b),le(y.$$.fragment,b),V=$(b),w=k(b,"BUTTON",{class:!0,"data-svelte-h":!0}),H(w)!=="svelte-1fyfwn0"&&(w.textContent=M),b.forEach(v),L=$(c),E&&E.l(c),D=$(c),N=k(c,"BUTTON",{class:!0,"data-svelte-h":!0}),H(N)!=="svelte-1aajpiv"&&(N.textContent=z),d=$(c),T&&T.l(c),A=Z(),this.h()},h(){u(l,"name","title"),u(l,"type","text"),u(l,"class","update__title svelte-lb1h5m"),u(i,"for","title"),u(i,"class","svelte-lb1h5m"),u(a,"class","update__title-wrapper svelte-lb1h5m"),u(o,"name","language"),u(o,"type","text"),u(o,"class","update__language svelte-lb1h5m"),u(_,"for","language"),u(_,"class","svelte-lb1h5m"),u(f,"class","update__language-wrapper svelte-lb1h5m"),u(w,"class","button update__delete svelte-lb1h5m"),u(e,"class","update__header svelte-lb1h5m"),u(N,"class","button update__add svelte-lb1h5m")},m(c,b){U(c,e,b),h(e,a),h(a,l),R(l,t[3].title),h(a,n),h(a,i),h(e,p),h(e,f),h(f,o),R(o,t[3].language),h(f,r),h(f,_),h(e,P),se(y,e,null),h(e,V),h(e,w),U(c,L,b),E&&E.m(c,b),U(c,D,b),U(c,N,b),U(c,d,b),T&&T.m(c,b),U(c,A,b),W=!0,G||(q=[J(l,"input",t[9]),J(o,"input",t[10]),J(w,"click",t[12]),J(N,"click",t[6])],G=!0)},p(c,b){b&8&&l.value!==c[3].title&&R(l,c[3].title),b&8&&o.value!==c[3].language&&R(o,c[3].language);const X={};!C&&b&8&&(C=!0,X.isChecked=c[3].is_published,me(()=>C=!1)),y.$set(X),c[3].cards?E?E.p(c,b):(E=_e(c),E.c(),E.m(D.parentNode,D)):E&&(E.d(1),E=null),b&12&&(I=JSON.stringify(c[2])!==JSON.stringify(c[3])),I?T?T.p(c,b):(T=de(c),T.c(),T.m(A.parentNode,A)):T&&(T.d(1),T=null)},i(c){W||(j(y.$$.fragment,c),W=!0)},o(c){F(y.$$.fragment,c),W=!1},d(c){c&&(v(e),v(L),v(D),v(N),v(d),v(A)),ae(y),E&&E.d(c),T&&T.d(c),G=!1,be(q)}}}function _e(t){let e,a=re(t[3].cards),l=[];for(let n=0;n<a.length;n+=1)l[n]=fe(ue(t,a,n));return{c(){for(let n=0;n<l.length;n+=1)l[n].c();e=Z()},l(n){for(let i=0;i<l.length;i+=1)l[i].l(n);e=Z()},m(n,i){for(let s=0;s<l.length;s+=1)l[s]&&l[s].m(n,i);U(n,e,i)},p(n,i){if(i&136){a=re(n[3].cards);let s;for(s=0;s<a.length;s+=1){const p=ue(n,a,s);l[s]?l[s].p(p,i):(l[s]=fe(p),l[s].c(),l[s].m(e.parentNode,e))}for(;s<l.length;s+=1)l[s].d(1);l.length=a.length}},d(n){n&&v(e),Se(l,n)}}}function fe(t){let e,a,l,n,i,s,p,f,o,r,_="🗑",O,P,y,C,V,w,M,L,D,N,z,d,I;function A(){t[13].call(a,t[21],t[22])}function W(){return t[14](t[22])}function G(){t[15].call(C,t[21],t[22])}return{c(){e=g("div"),a=g("input"),i=S(),s=g("label"),p=x("subtitle"),o=S(),r=g("button"),r.textContent=_,O=S(),P=g("div"),y=S(),C=g("textarea"),M=S(),L=g("label"),D=x("cheat-sheet content"),z=S(),this.h()},l(q){e=k(q,"DIV",{class:!0});var m=B(e);a=k(m,"INPUT",{class:!0,name:!0,id:!0}),i=$(m),s=k(m,"LABEL",{for:!0,class:!0});var K=B(s);p=ee(K,"subtitle"),K.forEach(v),o=$(m),r=k(m,"BUTTON",{class:!0,"data-svelte-h":!0}),H(r)!=="svelte-1p3ltd6"&&(r.textContent=_),O=$(m),P=k(m,"DIV",{class:!0}),B(P).forEach(v),y=$(m),C=k(m,"TEXTAREA",{class:!0,name:!0,id:!0}),B(C).forEach(v),M=$(m),L=k(m,"LABEL",{class:!0,for:!0});var E=B(L);D=ee(E,"cheat-sheet content"),E.forEach(v),z=$(m),m.forEach(v),this.h()},h(){u(a,"class","update__edit-card-title svelte-lb1h5m"),u(a,"name",l=`${t[3].id}_${t[22]}_title`),u(a,"id",n=`${t[3].id}_${t[22]}_title`),u(s,"for",f=`${t[3].id}_${t[22]}_title`),u(s,"class","svelte-lb1h5m"),u(r,"class","update__remove-card svelte-lb1h5m"),u(P,"class","update__edit-card-divider svelte-lb1h5m"),u(C,"class","update__edit-card-content svelte-lb1h5m"),u(C,"name",V=`${t[3].id}_${t[22]}`),u(C,"id",w=`${t[3].id}_${t[22]}`),u(L,"class","update__edit-card-label svelte-lb1h5m"),u(L,"for",N=`${t[3].id}_${t[22]}`),u(e,"class","update__edit-card-wrapper svelte-lb1h5m")},m(q,m){U(q,e,m),h(e,a),R(a,t[20].subtitle),h(e,i),h(e,s),h(s,p),h(e,o),h(e,r),h(e,O),h(e,P),h(e,y),h(e,C),R(C,t[20].content),h(e,M),h(e,L),h(L,D),h(e,z),d||(I=[J(a,"input",A),J(r,"click",W),J(C,"input",G)],d=!0)},p(q,m){t=q,m&8&&l!==(l=`${t[3].id}_${t[22]}_title`)&&u(a,"name",l),m&8&&n!==(n=`${t[3].id}_${t[22]}_title`)&&u(a,"id",n),m&8&&a.value!==t[20].subtitle&&R(a,t[20].subtitle),m&8&&f!==(f=`${t[3].id}_${t[22]}_title`)&&u(s,"for",f),m&8&&V!==(V=`${t[3].id}_${t[22]}`)&&u(C,"name",V),m&8&&w!==(w=`${t[3].id}_${t[22]}`)&&u(C,"id",w),m&8&&R(C,t[20].content),m&8&&N!==(N=`${t[3].id}_${t[22]}`)&&u(L,"for",N)},d(q){q&&v(e),d=!1,be(I)}}}function de(t){let e,a="Save",l,n;return{c(){e=g("button"),e.textContent=a,this.h()},l(i){e=k(i,"BUTTON",{class:!0,"data-svelte-h":!0}),H(e)!=="svelte-zer7oz"&&(e.textContent=a),this.h()},h(){u(e,"class","button update__save svelte-lb1h5m")},m(i,s){U(i,e,s),l||(n=J(e,"click",t[4]),l=!0)},p:Y,d(i){i&&v(e),l=!1,n()}}}function Ve(t){let e,a,l,n,i,s=t[0]&&ce(t);const p=[Ue,Ae],f=[];function o(r,_){return r[2]&&!r[1]?0:1}return l=o(t),n=f[l]=p[l](t),{c(){e=g("div"),s&&s.c(),a=S(),n.c(),this.h()},l(r){e=k(r,"DIV",{class:!0});var _=B(e);s&&s.l(_),a=$(_),n.l(_),_.forEach(v),this.h()},h(){u(e,"class","update__page svelte-lb1h5m")},m(r,_){U(r,e,_),s&&s.m(e,null),h(e,a),f[l].m(e,null),i=!0},p(r,[_]){r[0]?s?(s.p(r,_),_&1&&j(s,1)):(s=ce(r),s.c(),j(s,1),s.m(e,a)):s&&(oe(),F(s,1,1,()=>{s=null}),ie());let O=l;l=o(r),l===O?f[l].p(r,_):(oe(),F(f[O],1,1,()=>{f[O]=null}),ie(),n=f[l],n?n.p(r,_):(n=f[l]=p[l](r),n.c()),j(n,1),n.m(e,null))},i(r){i||(j(s),j(n),i=!0)},o(r){F(s),F(n),i=!1},d(r){r&&v(e),s&&s.d(),f[l].d()}}}function qe(t,e,a){let l,n;ne(t,we,d=>a(16,l=d)),ne(t,$e,d=>a(17,n=d));const i=n.params.id;let s=!1,p=!1,f,o;const r=async()=>{try{const d=await Oe(`/cheat_sheets/${i}`,l.token);a(2,f=d.data),a(3,o=structuredClone(f))}catch(d){console.log(d)}},_=async()=>{try{await ye(`/cheat_sheets/${i}`,l.token,{title:o.title,language:o.language,is_published:o.is_published,cards:o.cards}),a(2,f=structuredClone(o))}catch(d){console.log(d)}},O=async()=>{try{await Ne(`/cheat_sheets/${i}`,l.token),a(1,p=!0),a(0,s=!1),De("/dashboard")}catch(d){console.log(d)}},P=async()=>{o.cards?a(3,o.cards=[...o.cards,{subtitle:"",content:""}],o):a(3,o.cards=[{subtitle:"",content:""}],o)},y=async d=>{if(o.cards){const I=o.cards.filter((W,G)=>G!==d);a(3,o.cards=[...I],o);const A=document.activeElement;A&&A.blur()}};Ce(()=>{r()});function C(d){s=d,a(0,s)}function V(){o.title=this.value,a(3,o)}function w(){o.language=this.value,a(3,o)}function M(d){t.$$.not_equal(o.is_published,d)&&(o.is_published=d,a(3,o))}const L=()=>a(0,s=!0);function D(d,I){d[I].subtitle=this.value,a(3,o)}const N=d=>y(d);function z(d,I){d[I].content=this.value,a(3,o)}return[s,p,f,o,_,O,P,y,C,V,w,M,L,D,N,z]}class Fe extends ve{constructor(e){super(),ge(this,e,qe,Ve,he,{})}}export{Fe as component};
