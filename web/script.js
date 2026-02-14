// FounderOS Landing — Particles, Terminal Demo, Animations

// === Particle Constellation ===
(function(){
  var c=document.getElementById('particles');if(!c)return;
  var ctx=c.getContext('2d'),pts=[],w,h;
  function resize(){w=c.width=window.innerWidth;h=c.height=window.innerHeight}
  function init(){
    pts=[];var n=Math.min(70,Math.floor(w/18));
    for(var i=0;i<n;i++)pts.push({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*.35,vy:(Math.random()-.5)*.35,r:Math.random()*1.5+.5,o:Math.random()*.35+.08});
  }
  function draw(){
    ctx.clearRect(0,0,w,h);
    for(var i=0;i<pts.length;i++){
      var p=pts[i];p.x+=p.vx;p.y+=p.vy;
      if(p.x<0||p.x>w)p.vx*=-1;if(p.y<0||p.y>h)p.vy*=-1;
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle='rgba(139,92,246,'+p.o+')';ctx.fill();
      for(var j=i+1;j<pts.length;j++){
        var q=pts[j],dx=p.x-q.x,dy=p.y-q.y,d=dx*dx+dy*dy;
        if(d<20000){ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(q.x,q.y);ctx.strokeStyle='rgba(139,92,246,'+(0.07*(1-d/20000))+')';ctx.lineWidth=.5;ctx.stroke()}
      }
    }
    requestAnimationFrame(draw);
  }
  resize();init();draw();
  window.addEventListener('resize',function(){resize();init()});
})();

// === Hero Typing Effect ===
(function(){
  var el=document.getElementById('typeTarget');if(!el)return;
  var words=['never forgets.','ships every week.','thinks like a founder.','costs $0.','remembers everything.','replaces 5 hires.'];
  var wi=0,ci=0,del=false;
  function tick(){
    var w=words[wi];
    if(del){el.textContent=w.substring(0,--ci)}
    else{el.textContent=w.substring(0,++ci)}
    var sp=del?35:75;
    if(!del&&ci===w.length){sp=2200;del=true}
    else if(del&&ci===0){del=false;wi=(wi+1)%words.length;sp=400}
    setTimeout(tick,sp);
  }
  setTimeout(tick,800);
})();

// === Counter Animation ===
(function(){
  var nums=document.querySelectorAll('.hstat-num');
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(!e.isIntersecting)return;
      var el=e.target,target=parseInt(el.dataset.target),suffix=el.dataset.suffix||'',start=performance.now();
      (function upd(now){
        var p=Math.min((now-start)/2000,1),eased=1-Math.pow(1-p,3);
        el.textContent=Math.floor(target*eased).toLocaleString()+suffix;
        if(p<1)requestAnimationFrame(upd);
      })(start);
      obs.unobserve(el);
    });
  },{threshold:.5});
  nums.forEach(function(n){obs.observe(n)});
})();

// === Terminal Demo ===
(function(){
  var body=document.getElementById('termBody');if(!body)return;
  var lines=[
    {t:'cmd',p:'$ ',s:'git clone https://github.com/bibhubhushan/founder-os.git'},
    {t:'out',c:'success',s:'Cloning into \'founder-os\'... done.'},
    {t:'cmd',p:'$ ',s:'cd founder-os'},
    {t:'gap'},
    {t:'out',c:'success',s:'  \u2713 FounderOS v5.1 loaded'},
    {t:'out',c:'success',s:'  \u2713 5 agents online'},
    {t:'out',c:'success',s:'  \u2713 Memory system active'},
    {t:'out',c:'success',s:'  \u2713 Zero API keys required'},
    {t:'gap'},
    {t:'cmd',p:'> ',s:'/ceo What makes us hard to copy?'},
    {t:'gap'},
    {t:'out',c:'accent',s:'  \u25C6 ELON MODE (/ceo) \u2014 Big Picture'},
    {t:'out',c:'accent',s:'  \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501'},
    {t:'gap'},
    {t:'out',c:'output',s:'  Your edge isn\'t code. It\'s what you'},
    {t:'out',c:'output',s:'  learned along the way. Every decision'},
    {t:'out',c:'output',s:'  saved, every lesson kept. Others start'},
    {t:'out',c:'output',s:'  over every time. You never do.'},
    {t:'gap'},
    {t:'out',c:'dim',s:'  \u25B8 Track: big bets tested per week'},
    {t:'out',c:'dim',s:'  \u25B8 Next: /team_mvp to start building'},
  ];
  var li=0,ci=0,curLine=null,started=false;

  function mkLine(){var d=document.createElement('div');d.className='term-line';body.appendChild(d);return d}

  function step(){
    if(li>=lines.length){var cur=document.createElement('span');cur.className='term-cursor';body.appendChild(cur);return}
    var ln=lines[li];
    if(ln.t==='gap'){mkLine().innerHTML='&nbsp;';li++;setTimeout(step,80);return}
    if(ln.t==='cmd'){
      if(!curLine){curLine=mkLine();ci=0}
      if(ci<ln.s.length){
        ci++;var txt=ln.s.substring(0,ci);
        curLine.innerHTML='<span class="prompt">'+ln.p+'</span><span class="cmd">'+txt+'</span>';
        setTimeout(step,25+Math.random()*35);
      }else{curLine=null;li++;setTimeout(step,350)}
      body.scrollTop=body.scrollHeight;return;
    }
    var d=mkLine();d.innerHTML='<span class="'+(ln.c||'output')+'">'+ln.s+'</span>';
    li++;setTimeout(step,100);body.scrollTop=body.scrollHeight;
  }

  var tObs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){if(e.isIntersecting&&!started){started=true;setTimeout(step,400);tObs.unobserve(e.target)}});
  },{threshold:.25});
  tObs.observe(body.closest('.terminal')||body);
})();

// === Scroll Reveal ===
(function(){
  var els=document.querySelectorAll('.scroll-reveal');
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(!e.isIntersecting)return;
      var parent=e.target.parentElement;
      var sibs=Array.from(parent.children).filter(function(c){return c.classList.contains('scroll-reveal')});
      var idx=sibs.indexOf(e.target);
      setTimeout(function(){e.target.classList.add('visible')},idx*80);
      obs.unobserve(e.target);
    });
  },{threshold:.08,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(el){obs.observe(el)});
})();

// === Copy Install Command ===
(function(){
  var btn=document.getElementById('copyBtn'),code=document.getElementById('installCmd');
  if(!btn||!code)return;
  btn.addEventListener('click',function(){
    var text=code.textContent.replace(/\s+/g,' ').trim();
    if(navigator.clipboard){
      navigator.clipboard.writeText(text).then(ok).catch(fallback);
    }else{fallback()}
    function fallback(){var r=document.createRange();r.selectNodeContents(code);var s=window.getSelection();s.removeAllRanges();s.addRange(r);document.execCommand('copy');s.removeAllRanges();ok()}
    function ok(){btn.textContent='Copied!';btn.classList.add('copied');setTimeout(function(){btn.textContent='Copy';btn.classList.remove('copied')},2000)}
  });
})();

// === Card Parallax ===
(function(){
  document.querySelectorAll('.acard').forEach(function(card){
    card.addEventListener('mousemove',function(e){
      var r=card.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;
      var rx=(y-r.height/2)/25,ry=(r.width/2-x)/25;
      card.style.transform='translateY(-4px) perspective(1000px) rotateX('+rx+'deg) rotateY('+ry+'deg)';
    });
    card.addEventListener('mouseleave',function(){card.style.transform=''});
  });
})();

// === Smooth Scroll for Nav ===
document.querySelectorAll('a[href^="#"]').forEach(function(a){
  a.addEventListener('click',function(e){
    var target=document.querySelector(this.getAttribute('href'));
    if(target){e.preventDefault();target.scrollIntoView({behavior:'smooth',block:'start'})}
  });
});
