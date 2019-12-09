# todo-vue-cli

- TodoList component를 사용한 미니 프로젝트

## template

**반드시 최상단에는 1개의 태그만 존재가능**

- `components/TodoList.vue`

```html
// 다른 곳에서 사용할 컴포넌트를 생성
<div>
    <h2>{{ category }}</h2>
    ...
    <li v-for="todo in todos" :key="todo.id">
      <span>{{ todo.content }}</span>
		...
    </li>
  </div>
```

- `App.vue`

```html
// self closing tag 사용
// component load
<div>
    <TodoList category='todo'/>
    </div>
```

## script

- `components/TodoList.vue`

```javascript
<script>
export default {
  props: {
    ...
  },
  data: function() {
    return {
      ...
    };
  },
  methods: {
    addTodo: function() {
      ...
      }
    },
    removeTodo: function(todoId) {
      ...
      });
    }
  }
};
</script>
```

- `App.vue`

```javascript
<script>
// import <component> from '<상대경로>'
import TodoList from './components/TodoList.vue'
export default {
  components: {
    // TodoList: TodoList, // 이름이 같으면 생략해서 아래와 같이 쓸 수 있음
    TodoList,
  }
}
</script>
```

