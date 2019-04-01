---
layout: post
title: Android-MVP编程模式简介
subtitle: MVP编程模式、MVC比较
author: Kingtous
date: 2019-04-01 19:59:40
header-img: img/post-bg-miui6.jpg
catalog: True
tags:
- Android
typora-root-url: ../../Kingtous.github.io-master
---

## MVP简介

- M（model）负责数据的请求，解析，过滤等数据操作
- V（View）负责图示部分展示，图示事件处理，Activity，Fragment，Dialog，ViewGroup等呈现视图的组件都可以承担该角色
- P（presenter）是View和Model交互的桥梁。

拓展：

> **MVC简介**
>
> M(model)模型, 是应用程序中用于处理应用数据逻辑的部分，通常模型对象负责在数据库中进行存取
>
> V(view)视图， 是应用程序中处理数据的显示部分，通常视图是一句模型数据来创建的
>
> C(controller)控制器， 是应用程序中处理用户交互的部分，通常控制器负责从视图读取数据，控制用户的输入，并向模型发送数据。

*总结：你代码逻辑有没有写在View中的,有就是MVC,没有就是MVP*



## MVP类介绍

**Model**：框架中的模型超类，负责提供数据；

**View**：框架中的视图超类，负责UI展示；

**Presenter**：程序中的逻辑超类，负责处理具体事务；

**BaseMvp**：用于创建Model、View和Presenter；

**BasePresenter**：所有Presenter层的抽象类，负责Model、View层的引用和销毁；

**BaseMvpActivity**：Activity基类，具体的实现Model、View的绑定，我们自己的Activity可直接继承于此类或者自行实现BaseActivity继承于此类；

**BaseMvpFragment**：Fragment基类，具体作用和BaseMvpActivity相同。

  面向对象的原则告诉我们要针对接口编程，不要针对实现编程，所谓的针对接口编程不一定都是写一个类，并用implement来实现这个接口，而是泛指实现某个超类型的某个方法，这个超类型可以是类也可以是接口。秉承着这样的原则，我们设计出Mode、View、Presenter接口来充当所有类的父类（超类型），而具体的实现则有子类或者抽象子类来实现，这也是为什么我们所写的都是接口和抽象类，因为我们具体的实现都在我们自己的Activity或Fragment中，就像上图中展示的一样，红框内的代码和下面的是完全解耦的，方便我们移植到不同的项目中。

## 代码解读

- Model层

```
public interface Model {
}
```

> Model接口，用于数据模型的获取，所有子Mode类都要实现这个接口

- View层

```
public interface View {
    void showToast(String info);

    void showProgress();
}
```

>   View接口，所有视图类的父类，在接口中可以做一些基本的展示过程，比如Toast、Progress的显示，或者检查网络状态后的提醒，具体的实现由子类决定，子类也可以仍然是一个接口，继续拓展View的功能

- Presenter层

```
public interface Presenter<M extends Model, V extends View> {
    /**
     * 注册Model层
     *
     * @param model
     */
    void registerModel(M model);

    /**
     * 注册View层
     *
     * @param view
     */
    void registerView(V view);

    /**
     * 获取View
     *
     * @return
     */
    V getView();

    /**
     * 销毁动作（如Activity、Fragment的卸载）
     */
    void destroy();
}
```

>   这里的Presenter接口可能和想象的不太一样，可以看到这里面没有具体的业务逻辑方法，而是一些注册Mode和View层的抽象方法，在这里我们也可以获取传过来的View和Model，实际上这个接口更像是一个具有setter和getter的类。

  到这里，我们MVP框架的Model、View和Presenter层都出现了，但我们不可能在项目中直接implement来使用它们，因为那样会产生太多重复性的代码，并且不够简洁，我们还需要一些抽象类来实现一些公共的方法，最起码让Activity和Fragment能拿过来直接使用才能达到我们预期的目标。

- BasePresenter

```
public abstract class BasePresenter<M extends Model, V extends View> implements Presenter<M, V> {
    /**
     * 使用弱引用来防止内存泄漏
     */
    private WeakReference<V> wrf;
    protected M model;

    @Override
    public void registerModel(M model) {
        this.model = model;
    }

    @Override
    public void registerView(V view) {
        wrf = new WeakReference<V>(view);
    }

    @Override
    public V getView() {
        return wrf == null ? null : wrf.get();
    }

    /**
     * 在Activity或Fragment卸载时调用View结束的方法
     */
    @Override
    public void destroy() {
        if (wrf != null) {
            wrf.clear();
            wrf = null;
        }
        onViewDestroy();
    }

    protected abstract void onViewDestroy();
}
```

>   BasePresenter是我们要直接继承使用的Presenter层父类，它实现了Presenter接口中的抽象方法，并且为了防止内存泄漏，我们View层的引用要使用弱引用。**在MVP模式中，内存泄漏的主要原因是由于当前View层（如Activity或者Fragment）在卸载时，Model层中仍有业务没有结束（如子线程未完成、网络请求超时等），而这里的Presenter层中拥有Mode层和View层的引用，所以Presenter层也暂时无法释放，最终导致View的引用也没有释放，我们的Activity或者Fragment就算时销毁了，GC也无法回收它们，因为还有引用在指向它们呢。**
>    我们也不必非要使用弱引用来维护View层，其实在View层卸载时，只要主动让指向View的引用为空，也可以让Activity或者Fragment顺利回收，而且在View卸载时我们也可以选择是否停止当前Model层的业务，在BasePresenter类中，我们也同样实现了这个逻辑，就是destroy()方法，它通过调用onViewDestroy()来让具体实现这个方法的类来完成相应的业务逻辑。
>    在这里，我们仍然没有看到于项目有关的业务逻辑，这就对了，因为我们写的是一个MVP模式的框架，不是自己去写一个MVP模式的具体项目。

- BaseMvp

```
public interface BaseMvp<M extends Model, V extends View, P extends BasePresenter> {
    M createModel();

    V createView();

    P createPresenter();
}
```

>   BaseMvp是用来创建Model、View和Presenter层的，我们的MVP框架只去调用它们，具体的实现由真正的View层来做

- BaseMvpActivity

```
public abstract class BaseMvpActivity<M extends Model, V extends View, P extends BasePresenter> extends AppCompatActivity implements BaseMvp<M, V, P> {
    protected P presenter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //创建Presenter
        presenter = createPresenter();
        if (presenter != null) {
            //将Model层注册到Presenter中
            presenter.registerModel(createModel());
            //将View层注册到Presenter中
            presenter.registerView(createView());
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (presenter != null) {
            //Activity销毁时的调用，让具体实现BasePresenter中onViewDestroy()方法做出决定
            presenter.destroy();
        }
    }
}
```

>   这是Activity基类（只是对我们MVP框架来说，我们完全可以在项目中再写一个BaseActivity来继承它，实现基类真正的功能），我们以后所写的Activity都要继承它，并实现它的抽象方法和BaseMvp中的接口。它的主要功能就是创建Model、View、Presenter层并注册。这里我们也看到了上面提到的BasePresenter中destroy()方法具体调用的地方，就是在Activity中的onDestroy()中。

- BaseMvpFragment

```
public abstract class BaseMvpFragment<M extends Model, V extends View, P extends BasePresenter> extends Fragment implements BaseMvp<M, V, P> {
    protected P presenter;

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);

        presenter = createPresenter();
        if (presenter != null) {
            presenter.registerModel(createModel());
            presenter.registerView(createView());
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        if (presenter != null) {
            presenter.destroy();
        }
    }
}
```

> 这是Fragment基类，基本上和BaseMvpActivity类如出一辙，在这里就不再赘述了。

## 使用

  现在回过头来再看看刚开始的UML类图。红框中的类和接口我们都已经完成了，他们之间的关系也理清了，接口中定义了我们要做的事情，抽象类中为我们确定了Mode、View和Presenter彼此之间的联系，他们之间的该发生的不该发生的事情我们都已经搞定了，但这仅仅才刚开始，我们最终的目的是要使用他们。
   我们先使用Activity，在UML类图中我们可以看到MainActivity的继承关系，其实它可以直接继承于BaseMvpActivity，我们这里是自己实现的BaseActivity然后再继承之，

- 项目中的Model和它的实现类

```
public interface MainModel extends Model {
    /**
     * 从网络获取数据
     *
     * @return
     */
    String getDataFromNet();

    /**
     * 停止请求
     */
    void stopRequest();
}
public class MainModelImpl implements MainModel {
    @Override
    public String getDataFromNet() {
        return "MVP 模式,into fragment";
    }

    @Override
    public void stopRequest() {
        Log.i("MainModelImpl", "stop request...");
    }
}
```

- View和它的实现类

```
public interface MainView extends View {
    /**
     * 设置数据
     *
     * @param str
     */
    void setData(String str);
}
public class MainActivity extends BaseActivity<MainModel, MainView, MainPresenter> implements MainView {
    private TextView tvFirst;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvFirst = findViewById(R.id.tv_first);
        tvFirst.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, SecondActivity.class));
            }
        });
        init();
    }


    @Override
    public MainModel createModel() {
        return new MainModelImpl();
    }

    @Override
    public MainView createView() {
        return this;
    }

    @Override
    public MainPresenter createPresenter() {
        return new MainPresenter();
    }

    private void init() {
        if (presenter != null) {
            presenter.getData();
        }
    }

    @Override
    public void setData(String str) {
        tvFirst.setText(str);
    }
}
```

> createModel()、createView()和createPresenter()实现了BaseMvpActivity中的抽象方法，真正返回了具体的M、V、P层

- Presenter层

```java
public class MainPresenter extends BasePresenter<MainModel, MainView> {
    public void getData() {//这里要注意判空（view和model可能为空）
        String dataFromNet = null;
        if (model != null) {
            dataFromNet = model.getDataFromNet();
        }
        if (getView() != null) {
            getView().setData(dataFromNet);
        }
    }

    @Override
    protected void onViewDestroy() {//销毁Activity时的操作，可以停止当前的model
        if (model != null) {
            model.stopRequest();
        }
    }
}
```

> Presenter层没有实现接口，而是继承了BasePresenter抽象类，在这个类中，我们可以通过getView()方法来获取VIew层，直接拿去model来获取Model层的实例，但这一切一定要注意判空。

## 结合RxJava及Retrofit使用

  此框架结合RxJava和Retrofit会更加方便，Retrofit本身支持RxJava，所以我们只需要在Model层中返回Observable到Presenter中即可，在Presenter中等待网络请求的结束，并通知View层。看一下代码。

- Model和它的实现类

```java
public interface MainModel extends Model {
    /**
     * 从网络获取数据
     *
     * @return
     */
    Observable<List<User>> getDataFromNet();

    String getDataFromString();

    /**
     * 停止请求
     */
    void stopRequest();
}
interface GitHubService {
        @GET("user.json")
        Observable<List<User>> getUser();
    }

    @Override
    public Observable<List<User>> getDataFromNet() {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("https://www.icandemy.cn/")
                .addConverterFactory(GsonConverterFactory.create())
                .addCallAdapterFactory(RxJava2CallAdapterFactory.createWithScheduler(new IoScheduler()))
                .build();
        GitHubService gitHubService = retrofit.create(GitHubService.class);
        return gitHubService.getUser();
    }
```

- Presenter层

```java
public void getData() {//这里要注意判空（view和model可能为空）
        if (model != null) {
            Observable<List<User>> observable = model.getDataFromNet();
            observable.observeOn(AndroidSchedulers.mainThread()).subscribe(new Observer<List<User>>() {
                @Override
                public void onSubscribe(Disposable d) {
                }

                @Override
                public void onNext(List<User> users) {
                    if (getView() != null) {
                        getView().setData(new Gson().toJson(users));
                    }
                }

                @Override
                public void onError(Throwable e) {
                }

                @Override
                public void onComplete() {
                }
            });
        }
    }
```

## 实例：Google Sample TodoAPP架构

![](/img/Android/todo-mvp_structure.png)



### 参考

[简书](https://www.jianshu.com/p/51c4681f7f94)