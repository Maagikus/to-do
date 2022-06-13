(() => {
    "use strict";
    function isWebp() {
        function testWebP(callback) {
            let webP = new Image;
            webP.onload = webP.onerror = function() {
                callback(2 == webP.height);
            };
            webP.src = "data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA";
        }
        testWebP((function(support) {
            let className = true === support ? "webp" : "no-webp";
            document.documentElement.classList.add(className);
        }));
    }
    let addWindowScrollEvent = false;
    setTimeout((() => {
        if (addWindowScrollEvent) {
            let windowScroll = new Event("windowScroll");
            window.addEventListener("scroll", (function(e) {
                document.dispatchEvent(windowScroll);
            }));
        }
    }), 0);
    document.addEventListener("DOMContentLoaded", (event => {
        function onPageLoaded(key) {
            const todoList = document.querySelector(".todo__body");
            const data = localStorage.getItem("todo");
            function loadTodos() {
                if (data) todoList.innerHTML = data;
            }
            loadTodos();
            function addTodo() {
                const inp = document.querySelector(".todo__input").value;
                document.querySelectorAll(".todo__item");
                if (inp.length > 3) {
                    const item = ` <li class="todo__item" draggable="true" >\n            \n            \n                ${inp}\n            \n            \n            <button class="todo__del">Dell</button>\n        </li>`;
                    todoList.insertAdjacentHTML("beforeend", item);
                    document.querySelector("input").value = "";
                    dragEndDrop();
                }
                return inp;
            }
            document.addEventListener("click", (event => {
                let targetItem = event.target;
                if (targetItem.closest(".todo__add")) addTodo();
                if (targetItem.closest(".todo__del")) {
                    document.querySelector(".todo__item");
                    targetItem.parentElement.style.opacity = "0";
                    targetItem.parentElement.style.transition = ".9s";
                    targetItem.parentElement.addEventListener("transitionend", (function() {
                        this.remove();
                    }));
                }
                if (targetItem.closest(".todo__item")) targetItem.classList.toggle("_done");
                if (targetItem.closest(".todo__save")) localStorage.setItem("todo", todoList.innerHTML);
                if (targetItem.closest(".todo__clear")) localStorage.removeItem("todo", todoList.innerHTML);
                if (targetItem.closest(".todo__delete")) todoList.innerHTML = "";
                if (targetItem.closest(".todo__open")) todoList.innerHTML = localStorage.getItem("todo");
            }));
        }
        onPageLoaded();
        const dragEndDrop = function() {
            const tasksListElement = document.querySelector(`.todo__body`);
            const taskElements = tasksListElement.querySelectorAll(`.todo__item`);
            for (const task of taskElements) task.draggable = true;
            tasksListElement.addEventListener(`dragstart`, (evt => {
                evt.target.classList.add(`selected`);
            }));
            tasksListElement.addEventListener(`dragend`, (evt => {
                evt.target.classList.remove(`selected`);
            }));
            const getNextElement = (cursorPosition, currentElement) => {
                const currentElementCoord = currentElement.getBoundingClientRect();
                const currentElementCenter = currentElementCoord.y + currentElementCoord.height / 2;
                const nextElement = cursorPosition < currentElementCenter ? currentElement : currentElement.nextElementSibling;
                return nextElement;
            };
            tasksListElement.addEventListener(`dragover`, (evt => {
                evt.preventDefault();
                evt.stopPropagation();
                const activeElement = tasksListElement.querySelector(`.selected`);
                const currentElement = evt.target;
                const isMoveable = activeElement !== currentElement && currentElement.classList.contains(`todo__item`);
                if (!isMoveable) return;
                const nextElement = getNextElement(evt.clientY, currentElement);
                if (nextElement && activeElement === nextElement.previousElementSibling || activeElement === nextElement) return;
                tasksListElement.insertBefore(activeElement, nextElement);
            }));
        };
    }));
    window["FLS"] = true;
    isWebp();
})();