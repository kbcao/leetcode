class LinkedNode {
public:
	LinkedNode * l, *r;
	int key, value;

	LinkedNode(int k, int v) : key(k), value(v) {
		l = r = nullptr;
	}
};

class LRUCache {
public:
	unordered_map<int, LinkedNode*> keys;
	LinkedNode *head;

	LRUCache(int capacity) {
		ios::sync_with_stdio(false);
		LinkedNode *node = head = new LinkedNode(-1, -1);
		for (int i = 0; i < capacity; ++i) {
			LinkedNode *last = new LinkedNode(-1, -1);
			node->r = last;
			last->l = node;
			node = last;
		}
		node->r = head;
		head->l = node;
	}

	int get(int key) {
		if (keys.find(key) == keys.end()) return -1;
		LinkedNode *res = keys[key];
		move_to_head(res);
		return res->value;
	}

	void put(int key, int value) {
		if (keys.find(key) == keys.end()) {
			LinkedNode *res = keys[key] = head->l;
			move_to_head(res);
			if (keys.find(res->key) != keys.end()) keys.erase(res->key);
			res->key = key;
			res->value = value;
		}
		else {
			LinkedNode *res = keys[key];
			move_to_head(res);
			res->value = value;
		}
	}

	void move_to_head(LinkedNode *node) {
		node->l->r = node->r;
		node->r->l = node->l;
		head->r->l = node;
		node->r = head->r;
		node->l = head;
		head->r = node;
	}

	void print() {
		auto node = head;
		while (node != head->l) {
			cout << "[" << node->l << ", " << node->key << ", " << node << ", " << node->value << ", " << node->r << "] ";
			node = node->r;
		}
		cout << "[" << node->l << ", " << node->key << ", " << node << ", " << node->value << ", " << node->r << "] " << endl;
	}
};